import base64
from unittest.mock import AsyncMock, patch, MagicMock
import os
import pytest
import sys
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lmnt')))
from api import Speech, StreamingSynthesisConnection, _SYNTHESIZE_STREAMING_ENDPOINT  # noqa


MOCK_AUDIO = 'UklGRiQAAABXQVZFZm10IBAAAAABAAEAIlYAAESsAAACABAAZGF0YQAAAAA='
MOCK_RESPONSE_OBJ = {'audio': MOCK_AUDIO, 'durations': [{'text': 'Hello,', 'start': 0.0,
                                                         'duration': 0.5}, {'text': 'world!', 'start': 0.5, 'duration': 0.5}], 'seed': 'random_seed'}


@pytest.fixture
async def api():
  with patch('aiohttp.ClientSession', new=MagicMock()) as MockClientSession:
    key = 'test_key'
    api = Speech(key)
    api._lazy_init()
    MockClientSession.assert_called_once()
    yield api


@pytest.mark.asyncio
async def test_synthesize(api):
  text = 'Hello, world!'
  voice = 'Voice1'
  mock_response = {'audio': MOCK_AUDIO, 'durations': [], 'seed': 'random_seed'}
  api._session.post.return_value.__aenter__.return_value.json = AsyncMock(return_value=mock_response)
  api._session.post.return_value.__aenter__.return_value.status = 200

  synthesis_result = await api.synthesize(text, voice)
  assert synthesis_result == {'audio': base64.b64decode(mock_response['audio'])}


@pytest.mark.asyncio
async def test_synthesize_return_durations(api):
  text = 'Hello, world!'
  voice = 'Voice1'
  mock_response = MOCK_RESPONSE_OBJ
  api._session.post.return_value.__aenter__.return_value.json = AsyncMock(return_value=mock_response)
  api._session.post.return_value.__aenter__.return_value.status = 200

  synthesis_result = await api.synthesize(text, voice, return_durations=True)
  assert synthesis_result == {'audio': base64.b64decode(mock_response['audio']), 'durations': mock_response['durations']}


@pytest.mark.asyncio
async def test_synthesize_return_seed(api):
  text = 'Hello, world!'
  voice = 'Voice1'
  mock_response = {'audio': MOCK_AUDIO, 'durations': [], 'seed': 'random_seed'}
  api._session.post.return_value.__aenter__.return_value.json = AsyncMock(return_value=mock_response)
  api._session.post.return_value.__aenter__.return_value.status = 200

  synthesis_result = await api.synthesize(text, voice, return_seed=True)
  assert synthesis_result == {'audio': base64.b64decode(mock_response['audio']), 'seed': mock_response['seed']}


@pytest.mark.asyncio
async def test_synthesize_return_durations_and_seed(api):
  text = 'Hello, world!'
  voice = 'Voice1'
  mock_response = MOCK_RESPONSE_OBJ
  api._session.post.return_value.__aenter__.return_value.json = AsyncMock(return_value=mock_response)
  api._session.post.return_value.__aenter__.return_value.status = 200

  synthesis_result = await api.synthesize(text, voice, return_durations=True, return_seed=True)
  assert synthesis_result == {'audio': base64.b64decode(mock_response['audio']), 'durations': mock_response['durations'], 'seed': mock_response['seed']}


@pytest.mark.asyncio
async def test_synthesize__non_en_language(api):
  text = 'Hello, world!'
  voice = 'Voice1'
  language = 'pt'
  mock_response = {'audio': MOCK_AUDIO, 'durations': [], 'seed': 'random_seed'}
  api._session.post.return_value.__aenter__.return_value.json = AsyncMock(return_value=mock_response)
  api._session.post.return_value.__aenter__.return_value.status = 200

  synthesis_result = await api.synthesize(text, voice, language=language)
  assert synthesis_result == {'audio': base64.b64decode(mock_response['audio'])}


@pytest.mark.asyncio
async def test_synthesize_no_text(api):
  with pytest.raises(AssertionError):
    await api.synthesize(None, 'Voice1')


@pytest.mark.asyncio
async def test_synthesize_no_voice(api):
  with pytest.raises(AssertionError):
    await api.synthesize('Hello, world!', None)


@pytest.mark.asyncio
async def test_deprecated_durations(api):
  text = 'Hello, world!'
  voice = 'Voice1'
  mock_response = MOCK_RESPONSE_OBJ
  api._session.post.return_value.__aenter__.return_value.json = AsyncMock(return_value=mock_response)
  api._session.post.return_value.__aenter__.return_value.status = 200

  synthesis_result = await api.synthesize(text, voice, durations=True)
  assert synthesis_result == {'audio': base64.b64decode(mock_response['audio']), 'durations': mock_response['durations']}


@pytest.mark.asyncio
async def test_deprecated_durations_false(api):
  text = 'Hello, world!'
  voice = 'Voice1'
  mock_response = MOCK_RESPONSE_OBJ
  api._session.post.return_value.__aenter__.return_value.json = AsyncMock(return_value=mock_response)
  api._session.post.return_value.__aenter__.return_value.status = 200

  synthesis_result = await api.synthesize(text, voice, durations=False, return_durations=True)
  assert synthesis_result == {'audio': base64.b64decode(mock_response['audio']), 'durations': mock_response['durations']}


@pytest.mark.asyncio
async def test_synthesize_streaming(api):
  voice = 'Voice1'
  speed = 1.5
  expressive = 0.8
  return_extras = True
  language = 'pt'

  mock_ws = AsyncMock()
  api._session = AsyncMock()
  api._session.ws_connect.return_value = mock_ws

  connection = await api.synthesize_streaming(voice, return_extras=return_extras, speed=speed, expressive=expressive, language=language)

  assert isinstance(connection, StreamingSynthesisConnection)
  api._session.ws_connect.assert_called_once_with(f'{api._base_url}{_SYNTHESIZE_STREAMING_ENDPOINT}')
  mock_ws.send_str.assert_called_once_with(json.dumps({
      'X-API-Key': api._api_key,
      'voice': voice,
      'speed': speed,
      'expressive': expressive,
      'send_extras': return_extras,
      'language': language
  }))


@pytest.mark.asyncio
async def test_synthesize_streaming_defaults(api):
  voice = 'Voice1'

  mock_ws = AsyncMock()
  api._session = AsyncMock()
  api._session.ws_connect.return_value = mock_ws

  connection = await api.synthesize_streaming(voice)

  assert isinstance(connection, StreamingSynthesisConnection)
  api._session.ws_connect.assert_called_once_with(f'{api._base_url}{_SYNTHESIZE_STREAMING_ENDPOINT}')
  mock_ws.send_str.assert_called_once_with(json.dumps({
      'X-API-Key': api._api_key,
      'voice': voice,
      'send_extras': False
  }))
