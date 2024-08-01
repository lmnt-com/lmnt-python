# Copyright 2023 LMNT, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from aiohttp import WSMsgType
from typing import List, Optional

import aiohttp
import base64
import json
import os


_BASE_URL = 'https://api.lmnt.com'
_SYNTHESIZE_STREAMING_ENDPOINT = '/v1/ai/speech/stream'
_LIST_VOICES_ENDPOINT = '/v1/ai/voice/list'
_VOICE_ENDPOINT = '/v1/ai/voice/{id}'
_CREATE_VOICE_ENDPOINT = '/v1/ai/voice'
_SPEECH_ENDPOINT = '/v1/ai/speech'
_ACCOUNT_ENDPOINT = '/v1/account'


class SpeechError(Exception):
  def __init__(self, status, error, caller):
    self.message = ''
    if caller:
      self.message = f'[{caller}]: '
    self.status = status
    if 'error' in error:
      self.message += error['error']
    elif 'message' in error:
      self.message += error['message']
    else:
      self.message += 'Unknown error; see status code for hints on what went wrong.'

  def __str__(self):
    return f'SpeechError [status={self.status}] {self.message}'


class StreamError(Exception):
  def __init__(self, message):
    self.message = message

  def __str__(self):
    return f'StreamError: {self.message}'


class _StreamingSynthesisIterator:
  def __init__(self, original_iterator, return_extras: bool):
    self.original_iterator = original_iterator
    self.return_extras = return_extras

  async def __anext__(self):
    msg1 = await self.original_iterator.__anext__()
    if msg1.type == WSMsgType.CLOSE:
      return  # Equivalent to raising a StopAsyncIteration exception, will cleanly stop async for loop
    data = {}

    if self.return_extras:
      msg1_json = self._parse_and_check_errors(msg1, require_error=False)
      msg2 = await self.original_iterator.__anext__()
      if msg2.type != WSMsgType.BINARY:
        self._parse_and_check_errors(msg2)
      data = {'audio': msg2.data, 'durations': msg1_json['durations']}
      if 'warning' in msg1_json:
        data['warning'] = msg1_json['warning']
      if 'buffer_empty' in msg1_json:
        data['buffer_empty'] = msg1_json['buffer_empty']
    else:
      if msg1.type != WSMsgType.BINARY:
        self._parse_and_check_errors(msg1)
      data = {'audio': msg1.data}

    return data

  def _parse_and_check_errors(self, msg, require_error=True):
    if msg.type != WSMsgType.TEXT:
      raise StreamError('Unexpected message type received from server.')
    msg_json = json.loads(msg.data)
    if 'error' in msg_json:
      raise StreamError(msg_json['error'])
    if require_error:
      raise StreamError('Unexpected message type received from server.')
    return msg_json


class StreamingSynthesisConnection:
  def __init__(self, socket, return_extras: bool):
    self.socket = socket
    self.return_extras = return_extras

  def __aiter__(self):
    """
    Returns a streaming iterator that yields an object containing binary audio data (and optionally other data) as it is received from the server.
    """
    return _StreamingSynthesisIterator(self.socket.__aiter__(), self.return_extras)

  async def __anext__(self):
    return self.socket.__anext__()

  async def append_text(self, text: str):
    msg = {
        'text': text
    }
    await self.socket.send_str(json.dumps(msg))

  async def flush(self):
    await self.socket.send_str('{"flush": true}')

  async def finish(self):
    await self.socket.send_str('{"eof": true}')


class Speech:
  def __init__(self, api_key: Optional[str] = None, **kwargs):
    self._session = None
    self._api_key = api_key or os.environ.get('LMNT_API_KEY')
    self._base_url = kwargs.get('base_url', _BASE_URL)
    self._connector = kwargs.get('connector', None)
    if not self._api_key:
      raise ValueError('Please set the `LMNT_API_KEY` environment variable or pass it in to the Speech constructor.')

  async def __aenter__(self):
    self._lazy_init()
    return self

  async def __aexit__(self, exc_type, exc, tb):
    await self.close()

  async def close(self):
    if self._session is not None:
      await self._session.close()
    self._session = None

  async def list_voices(self, starred: bool = False, owner: str = 'all'):
    """
    Returns a list of voices available to you.

    Optional parameters:
    - `starred`: Show starred voices only. Defaults to `false`.
    - `owner`: Specify which voices to return. Choose from `system`, `me`, or `all`. Defaults to `all`.

    Returns a list of dictionaries containing details of each voice.
    """
    if owner not in ['all', 'system', 'me']:
      raise ValueError(f'Invalid owner: {owner}')
    if not isinstance(starred, bool):
      raise ValueError(f'Invalid starred: {starred}')
    self._lazy_init()
    url = f'{self._base_url}{_LIST_VOICES_ENDPOINT}?starred={starred}&owner={owner}'

    async with self._session.get(url, headers=self._build_headers()) as resp:
      await self._handle_response_errors(resp, 'Speech.list_voices')
      return await resp.json()

  async def voice_info(self, voice_id: str):
    """
    Returns details of a specific voice.

    Required parameters:
    - `voice_id`: The id of the voice to get info on. If you don't know the id, you can get it from `list_voices()`.

    Returns a dictionary containing details of the voice.
    """
    self._lazy_init()
    url = f'{self._base_url}{_VOICE_ENDPOINT}'.format(id=voice_id)

    async with self._session.get(url, headers=self._build_headers()) as resp:
      await self._handle_response_errors(resp, 'Speech.voice_info')
      return await resp.json()

  async def create_voice(self, name: str, enhance: bool, filenames: List[str], type: str = 'instant', gender: str = None, description: str = None):
    """
    Creates a new voice from a set of audio files. Returns the voice metadata object.

    Parameters:
    - `name`: The name of the voice.
    - `enhance`: For unclean audio with background noise, applies processing to attempt to improve quality. Not on by default as it can also degrade quality in some circumstances.
    - `filenames`: A list of filenames to use for the voice.

    Optional parameters:
    - `type`: The type of voice to create. Must be one of `instant` or `professional`. Defaults to `instant`.
    - `gender`: The gender of the voice, e.g. `male`, `female`, `nonbinary`. For categorization purposes. Defaults to `None`.
    - `description`: A description of the voice. Defaults to `None`.

    Returns the voice metadata object:
    - `id`: The id of the voice (`voice_id`).
    - `name`: The name of the voice.
    - `owner`: The owner of the voice.
    - `state`: The state of the voice, e.g. `ready`, `pending`, `broken`.
    - `gender`: The gender of the voice, e.g. `male`, `female`, `nonbinary`.
    - `type`: The type of voice, e.g. `instant`, `professional`.
    - `description`: A description of the voice.
    """
    if type not in ['instant', 'professional']:
      raise ValueError(f'[Speech.create_voice] Invalid type: {type}')
    if name is None:
      raise ValueError('[Speech.create_voice] Name must not be None.')
    if len(name) == 0:
      raise ValueError('[Speech.create_voice] Name must be non-empty.')
    if filenames is None:
      raise ValueError('[Speech.create_voice] Filenames must not be None.')
    if len(filenames) == 0:
      raise ValueError('[Speech.create_voice] Filenames must be non-empty.')
    if enhance is None:
      raise ValueError('[Speech.create_voice] Enhance must not be None.')

    self._lazy_init()

    metadata = json.dumps({
        'name': name,
        'enhance': enhance,
        'type': type,
        'gender': gender,
        'description': description,
    })
    files = []
    try:
      with aiohttp.MultipartWriter() as mpwriter:
        mpwriter.append(metadata, {'Content-Type': 'application/json', 'Content-Disposition': 'form-data; name="metadata"'})
        for filename in filenames:
          f = open(filename, 'rb')
          files.append(f)
          part = mpwriter.append(f)
          part.set_content_disposition('form-data', name='file_field', filename=os.path.basename(filename))
      async with self._session.post(f'{self._base_url}{_CREATE_VOICE_ENDPOINT}', data=mpwriter, headers=self._build_headers()) as resp:
        await self._handle_response_errors(resp, 'Speech.create_voice')
        return await resp.json()
    finally:
      for file in files:
        file.close()

  async def update_voice(self, voice_id: str, **kwargs):
    """
    Updates metadata for a specific voice. A voice that is not owned by you can only have its `starred` field updated.
    Only provided fields will be changed.

    Required parameters:
    - `voice_id` (str): The id of the voice to update. If you don't know the id, you can get it from `list_voices()`.

    Optional parameters:
    - `name` (str): The name of the voice.
    - `starred` (bool): Whether the voice is starred by you
    - `gender` (str):  The gender of the voice, e.g. `male`, `female`, `nonbinary`. For categorization purposes.
    - `description` (str): A description of the voice.
    """
    self._lazy_init()
    url = f'{self._base_url}{_VOICE_ENDPOINT}'.format(id=voice_id)

    data = {
        'name': kwargs.get('name', None),
        'starred': kwargs.get('starred', None),
        'gender': kwargs.get('gender', None),
        'description': kwargs.get('description', None),
    }
    data = json.dumps({k: v for k, v in data.items() if v is not None})
    async with self._session.put(url, data=data, headers=self._build_headers(type='application/json')) as resp:
      await self._handle_response_errors(resp, 'Speech.update_voice')
      return await resp.json()

  async def unfreeze_voice(self, voice_id: str):
    """
    Unfreezes a professional voice clone owned by you.

    We are constantly improving and releasing our speech models. Voices that are not being used will not be
    upgraded automatically and will enter a frozen state.

    Do not worry though. If your voice is frozen, call this method to upgrade it to the latest model.

    Instant voices always use the latest model and are never frozen.
    """
    self._lazy_init()
    url = f'{self._base_url}{_VOICE_ENDPOINT}'.format(id=voice_id)
    data = {
        'unfreeze': True
    }
    data = json.dumps({k: v for k, v in data.items() if v is not None})
    async with self._session.put(url, data=data, headers=self._build_headers(type='application/json')) as resp:
      await self._handle_response_errors(resp, 'Speech.unfreeze_voice')
      return await resp.json()

  async def delete_voice(self, voice_id: str):
    """
    Deletes a voice and cancels any pending operations on it. The voice must be owned by you. Cannot be undone.

    Required parameters:
    - `voice_id` (str): The id of the voice to delete. If you don't know the id, you can get it from `list_voices()`.
    """
    self._lazy_init()
    url = f'{self._base_url}{_VOICE_ENDPOINT}'.format(id=voice_id)

    async with self._session.delete(url, headers=self._build_headers()) as resp:
      await self._handle_response_errors(resp, 'Speech.delete_voice')
      return await resp.json()

  async def synthesize(self, text: str, voice: str, **kwargs):
    """
    Synthesize speech from text.

    Parameters:
    - `text` (str): The text to synthesize.
    - `voice` (str): The voice id to use for synthesis.

    Optional parameters:
    - `seed` (int): The seed used to specify a different take. Defaults to random.
    - `format` (str): The audio format to use for synthesis. Defaults to `mp3`.
    - `sample_rate` (int): 8000, 16000, or 24000 – the desired output sample rate. Defaults to 24000 for all formats except `mulaw` which defaults to 8000.
    - `speed` (float): Floating point value between 0.25 (slow) and 2.0 (fast); Defaults to 1.0
    - `return_durations` (bool): If `True`, the response will include word durations detail. Defaults to `False`.
    - `return_seed` (bool): If `True`, the response will include the seed used for synthesis. Defaults to `False`.
    - `language` (str): The desired language of the synthesized speech. Two letter ISO 639-1 code. Defaults to `en`.
    - `conversational` (bool): If `True`, the synthesized speech will be more conversational. Defaults to `False`.
    - `length` (int): The desired target length of the output speech in seconds. Maximum 300.0 (5 minutes)

    Deprecated parameters:
    - `durations` (bool): If `True`, the response will include word durations detail. Defaults to `False`. Deprecated in favor of `return_durations`.

    Returns an object with the following keys:
    - `audio`: The binary audio file.
    - `durations`: The word durations detail. Only returned if `return_durations` is `True`.
    - `seed`: The seed used for synthesis. Only returned if `return_seed` is `True`.

    Each `durations` entry is a dictionary describing the duration of each word with the following keys:
    - `text`: the word itself
    - `start`: the time at which the word starts, in seconds
    - `duration`: the overall duration of the word, in seconds
    """
    assert text is not None, '[Speech.synthesize] `text` must not be None.'
    assert voice is not None, '[Speech.synthesize] `voice` must not be None.'
    assert len(text) > 0, '[Speech.synthesize] `text` must be non-empty.'
    assert len(voice) > 0, '[Speech.synthesize] `voice` must be non-empty.'

    self._lazy_init()
    url = f'{self._base_url}{_SPEECH_ENDPOINT}'

    form_data = aiohttp.FormData()
    form_data.add_field('text', text)
    form_data.add_field('voice', voice)
    if 'seed' in kwargs:
      form_data.add_field('seed', kwargs.get('seed'))
    form_data.add_field('format', kwargs.get('format', 'mp3'))
    form_data.add_field('speed', kwargs.get('speed', 1.0))
    length = kwargs.get('length', None)
    if length is not None:
      form_data.add_field('length', length)
    if 'sample_rate' in kwargs:
      form_data.add_field('sample_rate', kwargs.get('sample_rate'))
    if 'quality' in kwargs:
      form_data.add_field('quality', kwargs.get('quality'))
    return_durations = kwargs.get('durations', False)
    if 'return_durations' in kwargs:  # return_durations takes precedence over durations
      return_durations = kwargs['return_durations']
    if return_durations is True:
      form_data.add_field('return_durations', 'true')
    return_seed = kwargs.get('return_seed', False)
    if 'language' in kwargs:
      form_data.add_field('language', kwargs.get('language'))
    if 'conversational' in kwargs:
      form_data.add_field('conversational', kwargs.get('conversational'))
    async with self._session.post(url, data=form_data, headers=self._build_headers()) as resp:
      await self._handle_response_errors(resp, 'Speech.synthesize')
      response_data = await resp.json()
      synthesis_result = {}
      synthesis_result['audio'] = base64.b64decode(response_data['audio'])
      if return_durations:
        synthesis_result['durations'] = response_data['durations']
      if return_seed:
        synthesis_result['seed'] = response_data['seed']
      return synthesis_result

  async def synthesize_streaming(self, voice: str, return_extras: bool = False, **kwargs):
    """
    Initiates a full-duplex streaming connection with the server that allows you to send text and receive audio in real-time.

    Parameters:
    - `format` (str): `mp3`, `raw`, or `ulaw` – the desired output format. Defaults to `mp3`.
    - `sample_rate` (int): 8000, 16000, or 24000 – the desired output sample rate. Defaults to 24000.
    - `voice` (str): The voice id to use for this connection.
    - `speed` (float): The speed to use for synthesis. Defaults to 1.0.
    - `return_extras` (bool): If `True`, the response will include word durations detail. Defaults to `False`.
    - `language` (str): The desired language of the synthesized speech. Two letter ISO 639-1 code. Defaults to `en`.
    - `conversational` (bool): If `True`, the synthesized speech will be more conversational. Defaults to `False`.

    Returns:
    - `StreamingSynthesisConnection`: The streaming connection object.
    """
    if not voice:
      raise ValueError('[Speech.synthesize_streaming] `voice` must not be None.')

    self._lazy_init()

    init_msg = {
        'X-API-Key': self._api_key,
        'voice': voice
    }
    if 'format' in kwargs:
      init_msg['format'] = kwargs['format']
    if 'sample_rate' in kwargs:
      init_msg['sample_rate'] = kwargs['sample_rate']
    if 'speed' in kwargs:
      init_msg['speed'] = kwargs['speed']
    if 'expressive' in kwargs:
      init_msg['expressive'] = kwargs['expressive']
    init_msg['send_extras'] = return_extras
    if 'language' in kwargs:
      init_msg['language'] = kwargs['language']
    if 'conversational' in kwargs:
      init_msg['conversational'] = kwargs['conversational']
    ws = await self._session.ws_connect(f'{self._base_url}{_SYNTHESIZE_STREAMING_ENDPOINT}')
    await ws.send_str(json.dumps(init_msg))
    return StreamingSynthesisConnection(ws, return_extras)

  async def account_info(self):
    """
    Returns details about your account.
    """
    self._lazy_init()
    url = f'{self._base_url}{_ACCOUNT_ENDPOINT}'

    async with self._session.get(url, headers=self._build_headers()) as resp:
      await self._handle_response_errors(resp, 'Speech.account_info')
      return await resp.json()

  def _lazy_init(self):
    if self._session is None:
      self._session = aiohttp.ClientSession(connector=self._connector)

  def _build_headers(self, type: str = None):
    headers = {'X-API-Key': self._api_key}
    if type is not None:
      headers['Content-Type'] = type
    return headers

  async def _handle_response_errors(self, response, caller=None):
    if response.status < 400:
      return
    raise SpeechError(response.status, await response.json(), caller)
