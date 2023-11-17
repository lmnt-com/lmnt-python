from unittest.mock import AsyncMock, patch, MagicMock
import os
import pytest
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lmnt')))
from api import Speech, _LIST_VOICES_ENDPOINT, _VOICE_ENDPOINT  # noqa


def test_lazy_init():
  with patch('aiohttp.ClientSession', new=MagicMock()) as MockClientSession:
    api = Speech('test_key')
    api._lazy_init()
    MockClientSession.assert_called_once()
    assert isinstance(api._session, MagicMock)


@pytest.fixture
def mock_response():
  return {
      'voices': [
          {'name': 'Voice1', 'language': 'en-US'},
          {'name': 'Voice2', 'language': 'en-GB'},
      ]
  }


@pytest.fixture
async def api():
  with patch('aiohttp.ClientSession', new=MagicMock()) as MockClientSession:
    key = 'test_key'
    api = Speech(key)
    api._lazy_init()
    MockClientSession.assert_called_once()
    yield api


@pytest.mark.asyncio
async def test_list_voices_default_params(api, mock_response):
  with patch('aiohttp.ClientSession', new=MagicMock()):
    api._session.get.return_value.__aenter__.return_value.json = AsyncMock(return_value=mock_response)
    api._session.get.return_value.__aenter__.return_value.status = 200
    result = await api.list_voices()
    api._session.get.assert_called_once_with(
        f'{api._base_url}{_LIST_VOICES_ENDPOINT}?starred=False&owner=all',
        headers=api._build_headers()
    )
    assert result == mock_response


@pytest.mark.asyncio
async def test_list_voices_with_params(api, mock_response):
  with patch('aiohttp.ClientSession', new=MagicMock()):
    api._session.get.return_value.__aenter__.return_value.json = AsyncMock(return_value=mock_response)
    api._session.get.return_value.__aenter__.return_value.status = 200
    result = await api.list_voices(starred=True, owner='me')
    api._session.get.assert_called_once_with(
        f'{api._base_url}{_LIST_VOICES_ENDPOINT}?starred=True&owner=me',
        headers=api._build_headers()
    )
    assert result == mock_response


@pytest.mark.asyncio
async def test_list_voices_with_params_system(api, mock_response):
  with patch('aiohttp.ClientSession', new=MagicMock()):
    api._session.get.return_value.__aenter__.return_value.json = AsyncMock(return_value=mock_response)
    api._session.get.return_value.__aenter__.return_value.status = 200
    result = await api.list_voices(starred=True, owner='system')
    api._session.get.assert_called_once_with(
        f'{api._base_url}{_LIST_VOICES_ENDPOINT}?starred=True&owner=system',
        headers=api._build_headers()
    )
    assert result == mock_response


@pytest.mark.asyncio
async def test_list_voices_invalid_owner(api):
  with pytest.raises(ValueError):
    await api.list_voices(owner='invalid')


@pytest.mark.asyncio
async def test_list_voices_starred(api):
  mock_response = [{'name': 'Voice1', 'starred': True}, {'name': 'Voice2', 'starred': True}]
  api._session.get.return_value.__aenter__.return_value.json = AsyncMock(return_value=mock_response)
  api._session.get.return_value.__aenter__.return_value.status = 200

  voices = await api.list_voices(starred=True)
  api._session.get.assert_called_once_with(
      f'{api._base_url}{_LIST_VOICES_ENDPOINT}?starred=True&owner=all',
      headers=api._build_headers()
  )
  assert voices == mock_response


@pytest.mark.asyncio
async def test_list_voices_invalid_star(api):
  with pytest.raises(ValueError):
    await api.list_voices(starred='invalid')


@pytest.mark.asyncio
async def test_voice_info(api):
  mock_response = {'id': 'Voice1', 'name': 'Voice1', 'language': 'en-US'}
  api._session.get.return_value.__aenter__.return_value.json = AsyncMock(return_value=mock_response)
  api._session.get.return_value.__aenter__.return_value.status = 200

  voice_info = await api.voice_info('Voice1')
  assert voice_info == mock_response


@pytest.mark.asyncio
async def test_voice_info_invalid_id(api):
  api._session.get.return_value.__aenter__.return_value.status = 400

  with pytest.raises(Exception):
    await api.voice_info('invalid')


@pytest.mark.asyncio
async def test_create_voice(api):
  mock_response = {'id': 'Voice1', 'name': 'Voice1', 'state': 'ready'}
  api._session.post.return_value.__aenter__.return_value.json = AsyncMock(return_value=mock_response)
  api._session.post.return_value.__aenter__.return_value.status = 200

  voice_info = await api.create_voice('Voice1', False, ['filename.wav', 'filename.wav'])
  assert voice_info == mock_response


@pytest.mark.asyncio
async def test_create_voice_invalid_type(api):
  with pytest.raises(ValueError):
    await api.create_voice('Voice1', False, ['filename.wav', 'filename.wav'], type='invalid')


@pytest.mark.asyncio
async def test_create_voice_no_name(api):
  with pytest.raises(ValueError):
    await api.create_voice(None, False, ['filename.wav', 'filename.wav'])


@pytest.mark.asyncio
async def test_create_voice_no_files(api):
  with pytest.raises(ValueError):
    await api.create_voice('Voice1', False, [])


@pytest.mark.asyncio
async def test_update_voice(api):
  mock_response = {'id': 'Voice1', 'name': 'UpdatedVoice', 'starred': True}
  api._session.put.return_value.__aenter__.return_value.json = AsyncMock(return_value=mock_response)
  api._session.put.return_value.__aenter__.return_value.status = 200

  voice_info = await api.update_voice('Voice1', name='UpdatedVoice', starred=True)
  assert voice_info == mock_response


@pytest.mark.asyncio
async def test_update_voice_invalid_id(api):
  api._session.put.return_value.__aenter__.return_value.status = 400

  with pytest.raises(Exception):
    await api.update_voice('invalid', name='UpdatedVoice', starred=True)


@pytest.mark.asyncio
async def test_delete_voice(api):
  voice_id = 'Voice1'
  api._session.delete.return_value.__aenter__.return_value.status = 200
  api._session.delete.return_value.__aenter__.return_value.json = AsyncMock(return_value={})

  response = await api.delete_voice(voice_id)
  api._session.delete.assert_called_once_with(
      f'{api._base_url}{_VOICE_ENDPOINT}'.format(id=voice_id),
      headers=api._build_headers()
  )
  assert response == {}


@pytest.mark.asyncio
async def test_delete_voice_invalid_id(api):
  api._session.delete.return_value.__aenter__.return_value.status = 400

  with pytest.raises(Exception):
    await api.delete_voice('invalid')
