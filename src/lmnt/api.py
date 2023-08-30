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
    self._base_url = kwargs.pop('base_url', _BASE_URL)

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
    assert text is not None, '[Speech.synthesize] `text` must not be None.'
    assert voice is not None, '[Speech.synthesize] `voice` must not be None.'
    assert len(text) > 0, '[Speech.synthesize] `text` must be non-empty.'
    assert len(voice) > 0, '[Speech.synthesize] `voice` must be non-empty.'

    self._lazy_init()
    url = f'{self._base_url}{_SYNTHESIZE_ENDPOINT}'

    form_data = aiohttp.FormData()
    form_data.add_field('text', text)
    form_data.add_field('voice', voice)
    form_data.add_field('seed', kwargs.pop('seed', 0))
    form_data.add_field('format', kwargs.pop('format', 'wav'))
    form_data.add_field('speed', kwargs.pop('speed', 1.0))
    async with self._session.post(url, data=form_data, headers=self._build_headers()) as resp:
      await self._handle_response_errors(resp)
      return await resp.read()

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
    return { 'X-API-Key': self._api_key }

  async def _handle_response_errors(self, response):
    if response.status < 400:
      return
    raise SpeechError(response.status, await response.json())
