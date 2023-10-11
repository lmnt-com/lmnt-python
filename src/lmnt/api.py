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

import aiohttp
import json

_BASE_URL = 'https://api.lmnt.com'
_VOICES_ENDPOINT = '/speech/beta/voices'
_SYNTHESIZE_ENDPOINT = '/speech/beta/synthesize'
_SYNTHESIZE_STREAMING_ENDPOINT = '/speech/beta/synthesize_streaming'
_SAMPLES_PER_FRAME = 300


class SpeechError(Exception):
  def __init__(self, status, error):
    self.status = status
    if 'error' in error:
      self.message = error['error']
    elif 'message' in error:
      self.message = error['message']
    else:
      'Unknown error; see status code for hints on what went wrong.'

  def __str__(self):
    return f'SpeechError [status={self.status}] {self.message}'


class StreamingSynthesisConnection:
  def __init__(self, socket):
    self.socket = socket

  def __aiter__(self):
    return self.socket.__aiter__()

  async def __anext__(self):
    return self.socket.__anext__()

  async def append_text(self, text):
    msg = {
        'text': text
    }
    await self.socket.send_str(json.dumps(msg))

  async def finish(self):
    await self.socket.send_str('{"eof": true}')


class Speech:
  def __init__(self, api_key: str, **kwargs):
    self._session = None
    self._api_key = api_key
    self._base_url = kwargs.get('base_url', _BASE_URL)

  async def __aenter__(self):
    self._lazy_init()
    return self

  async def __aexit__(self, exc_type, exc, tb):
    await self.close()

  async def close(self):
    if self._session is not None:
      await self._session.close()
    self._session = None

  async def list_voices(self):
    self._lazy_init()
    url = f'{self._base_url}{_VOICES_ENDPOINT}'

    async with self._session.get(url, headers=self._build_headers()) as resp:
      await self._handle_response_errors(resp)
      return (await resp.json())['voices']

  async def synthesize(self, text, voice, **kwargs):
    """
    Synthesize speech from text. Returns the binary audio data unless otherwise specified below.

    Parameters:
    - `text`: The text to synthesize.
    - `voice`: The voice id to use for synthesis.

    Optional parameters:
    - `seed`: The random seed to use for synthesis. Defaults to 0.
    - `format`: The audio format to use for synthesis. Defaults to `wav`.
    - `speed`: The speed to use for synthesis. Defaults to 1.0.
    - `durations`: If `True`, the response will include word durations detail. Defaults to `False`.
    - `length`: The desired target length of the output speech in seconds. Defaults to `None`.

    If `durations=True` is specified, the response will be a dictionary with the following keys:
    - `durations`: A list of dictionaries with keys as below.
    - `audio`: The binary audio data.

    Each `durations` entry is a dictionary with the following keys:
    - `phonemes`: A list of the phonemes comprising the word.
    - `phoneme_durations`: A list of the durations of each phoneme.
    - `start`: The starting duration of the word.
    - `duration`: The overall duration of the word.

    The audio sample rate is 24 kHz. Duration units are given in sample counts at 24kHz.
    """
    assert text is not None, '[Speech.synthesize] `text` must not be None.'
    assert voice is not None, '[Speech.synthesize] `voice` must not be None.'
    assert len(text) > 0, '[Speech.synthesize] `text` must be non-empty.'
    assert len(voice) > 0, '[Speech.synthesize] `voice` must be non-empty.'

    self._lazy_init()
    url = f'{self._base_url}{_SYNTHESIZE_ENDPOINT}'

    form_data = aiohttp.FormData()
    form_data.add_field('text', text)
    form_data.add_field('voice', voice)
    if 'seed' in kwargs:
      form_data.add_field('seed', kwargs.get('seed'))
    form_data.add_field('format', kwargs.get('format', 'wav'))
    form_data.add_field('speed', kwargs.get('speed', 1.0))
    length = kwargs.get('length', None)
    if length is not None:
      form_data.add_field('length', length)

    is_multipart_response = False
    extras = ''

    has_durations = kwargs.get('durations', False)
    if has_durations:
      extras = 'alignment'
      is_multipart_response = True

    if extras:
      form_data.add_field('extras', extras)

    async with self._session.post(url, data=form_data, headers=self._build_headers()) as resp:
      if is_multipart_response:
        response = await self._parse_multipart_alignment_response(resp)
        word_durations = self._transform_to_word_durations(response['duration'], response['phonemes'])
        return {
            'durations': word_durations,
            'audio': response['audio']
        }

      else:
        await self._handle_response_errors(resp)
        return await resp.read()

  def _transform_to_word_durations(self, durations, phonemes):
    if not durations or not phonemes or len(durations) != len(phonemes):
      raise ValueError("Invalid word durations input data.")

    result = []
    acc_phonemes, acc_durations = [], []
    total_duration, start = 0, 0

    for dur, phon in zip(durations, phonemes):
      if phon == " ":
        # Emit current accumulation if we have some.
        if len(acc_phonemes) > 0:
          result.append(self._create_duration_entry(
              acc_phonemes, acc_durations, start, total_duration))

        # Reset accumulation.
        start += total_duration
        acc_phonemes.clear()
        acc_durations.clear()

        # Emit the whitespace itself.
        duration_samples = dur * _SAMPLES_PER_FRAME
        total_duration = duration_samples
        result.append(self._create_duration_entry(
            [" "], [duration_samples], start, total_duration))
        start += total_duration
        total_duration = 0

      else:
        # Accumulate the phoneme.
        acc_phonemes.append(phon)
        duration_samples = dur * _SAMPLES_PER_FRAME
        acc_durations.append(duration_samples)
        total_duration += duration_samples

    # Emit any remaining accumulation.
    if len(acc_phonemes) > 0:
      result.append(self._create_duration_entry(
          acc_phonemes, acc_durations, start, total_duration))

    return result

  def _create_duration_entry(self, phonemes, durations, start, total_duration):
    return {
        'phonemes': phonemes.copy(),
        'phoneme_durations': durations.copy(),
        'start': start,
        'duration': total_duration
    }

  async def _get_next_content(self, reader):
    response = await reader.next()
    content_type = response.headers.get('Content-Type', '')
    # Note there are also `text` and `form` content types, but we don't need to handle those for now.
    return await response.json() if 'json' in content_type else await response.read()

  async def _parse_multipart_alignment_response(self, response):
    reader = aiohttp.MultipartReader.from_response(response)
    # Requesting alignment information returns a three-part multipart response:
    # 1. JSON of `duration` in frames.
    # 2. JSON of `phonemes`.
    # 3. Binary audio data.
    return {
        'duration': await self._get_next_content(reader),
        'phonemes': await self._get_next_content(reader),
        'audio': await self._get_next_content(reader)}

  async def synthesize_streaming(self, voice):
    self._lazy_init()

    init_msg = {
        'X-API-Key': self._api_key,
        'voice': voice
    }

    ws = await self._session.ws_connect(f'{self._base_url}{_SYNTHESIZE_STREAMING_ENDPOINT}')
    await ws.send_str(json.dumps(init_msg))
    return StreamingSynthesisConnection(ws)

  def _lazy_init(self):
    if self._session is None:
      self._session = aiohttp.ClientSession()

  def _build_headers(self):
    return {'X-API-Key': self._api_key}

  async def _handle_response_errors(self, response):
    if response.status < 400:
      return
    raise SpeechError(response.status, await response.json())
