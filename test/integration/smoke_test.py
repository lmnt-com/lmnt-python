import asyncio
import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'lmnt')))
from api import Speech, StreamingSynthesisConnection  # noqa

# Set an API key in your environment to run these tests
X_API_KEY = os.environ['X_API_KEY']
_BASE_URL = 'https://api.lmnt.com'


@pytest.fixture
async def api():
  async with Speech(X_API_KEY, base_url=_BASE_URL) as speech:
    yield speech


@pytest.mark.asyncio
async def test_init(api: Speech):
  assert api is not None


async def reader_task_binary(connection):
  async for msg in connection:
    assert msg is not None
    assert 'audio' in msg
    assert 'durations' not in msg


@pytest.mark.asyncio
async def test_synthesize_streaming(api: Speech):
  voice = 'lily'
  connection = await api.synthesize_streaming(voice)
  assert connection is not None
  assert isinstance(connection, StreamingSynthesisConnection)
  reader = asyncio.create_task(reader_task_binary(connection))
  await connection.append_text('One, Hello, world!')
  await connection.append_text('Two, Hello, world!')
  await connection.append_text('Three, Hello, world!')
  await connection.finish()
  await reader


async def reader_task_str(connection):
  async for msg in connection:
    assert msg is not None
    assert 'audio' in msg
    assert 'durations' in msg


@pytest.mark.asyncio
async def test_synthesize_streaming_return_extras(api: Speech):
  voice = 'lily'
  connection = await api.synthesize_streaming(voice, return_extras=True)
  assert connection is not None
  assert isinstance(connection, StreamingSynthesisConnection)
  reader = asyncio.create_task(reader_task_str(connection))
  await connection.append_text('One, Hello, world!')
  await connection.append_text('Two, Hello, world!')
  await connection.append_text('Three, Hello, world!')
  await connection.finish()
  await reader


@pytest.mark.asyncio
async def test_durations(api: Speech):
  voice = 'lily'
  text = 'Example Text'
  result = await api.synthesize(text=text, voice=voice, return_durations=True)
  assert result is not None
  assert 'durations' in result
  assert 'phonemes' not in result
  assert 'audio' in result
  assert len(result['durations']) > 0
  assert len(result['audio']) > 0
  assert isinstance(result['audio'], bytes)


@pytest.mark.asyncio
async def test_synthesize_with_invalid_voice(api: Speech):
  voice = 'invalid_voice'
  text = 'Example Text'
  with pytest.raises(Exception):
    await api.synthesize(text=text, voice=voice)


@pytest.mark.asyncio
async def test_synthesize_with_empty_text(api: Speech):
  voice = 'lily'
  text = ''
  with pytest.raises(Exception):
    await api.synthesize(text=text, voice=voice)


@pytest.mark.asyncio
async def test_synthesize(api: Speech):
  voice = 'lily'
  text = 'Example Text'
  result = await api.synthesize(text=text, voice=voice)
  assert result is not None
  assert 'audio' in result
  assert 'durations' not in result
  assert 'seed' not in result
  assert len(result['audio']) > 0
  assert isinstance(result['audio'], bytes)


@pytest.mark.asyncio
async def test_synthesize__non_en_language(api: Speech):
  voice = 'lily'
  text = 'Example Text'
  language = 'pt'
  result = await api.synthesize(text=text, voice=voice, language=language)
  assert result is not None
  assert 'audio' in result
  assert 'durations' not in result
  assert 'seed' not in result
  assert len(result['audio']) > 0
  assert isinstance(result['audio'], bytes)


@pytest.mark.asyncio
async def test_synthesize_with_empty_voice(api: Speech):
  voice = ''
  text = 'Example Text'
  with pytest.raises(Exception):
    await api.synthesize(text=text, voice=voice)


@pytest.mark.asyncio
async def test_list_voices(api: Speech):
  voices = await api.list_voices()
  assert isinstance(voices, list)
  assert len(voices) > 0


@pytest.mark.asyncio
async def test_list_voices_starred(api: Speech):
  voices = await api.list_voices(starred=True)
  assert isinstance(voices, list)


@pytest.mark.asyncio
async def test_list_voices_owned(api: Speech):
  voices = await api.list_voices(owner='me')
  assert isinstance(voices, list)


@pytest.mark.asyncio
async def test_list_voices_owned_system(api: Speech):
  voices = await api.list_voices(owner='system')
  assert isinstance(voices, list)


@pytest.mark.asyncio
async def test_get_voice(api: Speech):
  voice = await api.voice_info('lily')
  assert isinstance(voice, dict)
  assert voice['name'] == 'Lily'


@pytest.mark.asyncio
async def test_get_voice_with_invalid_voice(api: Speech):
  with pytest.raises(Exception):
    await api.voice_info('invalid_voice')


@pytest.mark.asyncio
async def test_update_voice_star(api: Speech):
  await api.update_voice('lily', starred=True)
  voice = await api.voice_info('lily')
  assert voice.get('starred') is True
  await api.update_voice('lily', starred=False)
  voice = await api.voice_info('lily')
  assert voice.get('starred') is False


@pytest.mark.asyncio
async def test_create_voice_basic_no_filenames(api: Speech):
  with pytest.raises(Exception):
    await api.create_voice(name='test_voice', enhance=True)


@pytest.mark.asyncio
async def test_create_voice_basic_empty_filenames(api: Speech):
  with pytest.raises(Exception):
    await api.create_voice(name='test_voice', enhance=True, filenames=[])


@pytest.mark.asyncio
async def test_create_voice_basic_no_enhance(api: Speech):
  with pytest.raises(Exception):
    await api.create_voice(name='test_voice', filenames=['filename.wav'])


@pytest.mark.asyncio
async def test_create_voice_basic_no_name(api: Speech):
  with pytest.raises(Exception):
    await api.create_voice(enhance=True, filenames=['filename.wav'])


@pytest.mark.asyncio
async def test_create_voice_basic_empty_name(api: Speech):
  with pytest.raises(Exception):
    await api.create_voice(name='', enhance=True, filenames=['filename.wav'])


@pytest.mark.asyncio
async def test_create_voice_basic_invalid_filenames(api: Speech):
  with pytest.raises(Exception):
    await api.create_voice(name='test_voice', enhance=True, filenames=['invalid_filename.wav'])


@pytest.mark.asyncio
async def test_create_voice_advanced(api: Speech):
  voice = await api.create_voice(name='integration_test_voice', enhance=True, filenames=['filename.wav'], description='test description', gender='male', type='instant')
  voice_id = voice['id']
  stored_voice = await api.voice_info(voice_id)
  await api.delete_voice(voice_id)
  assert voice['name'] == 'integration_test_voice'
  assert voice['owner'] == 'me'
  assert voice['state'] == 'ready'
  assert voice['type'] == 'instant'
  voice.pop('state')  # stored state is not set to ready immediately after creation
  stored_voice.pop('state')
  assert voice == stored_voice
  with pytest.raises(Exception):
    await api.voice_info(voice_id)


@pytest.mark.asyncio
async def test_update_owned_voice(api: Speech):
  original_voice = await api.create_voice(name='test_voice_update', enhance=True, filenames=['filename.wav'], description='test description', gender='male', type='instant')
  voice_id = original_voice['id']
  original_stored_voice = await api.voice_info(voice_id)
  updated_voice = await api.update_voice(voice_id, description='my new description', gender='female', name='integration_new_name', starred=False)
  updated_stored_voice = await api.voice_info(voice_id)
  await api.delete_voice(voice_id)
  updated_voice = updated_voice['voice']

  assert original_voice['name'] == 'test_voice_update'
  assert original_voice['owner'] == 'me'
  assert original_voice['state'] == 'ready'
  assert original_voice['type'] == 'instant'
  assert original_voice['description'] == 'test description'
  assert original_voice['gender'] == 'male'
  original_voice.pop('state')  # stored state is not set to ready immediately after creation
  original_stored_voice.pop('state')
  assert original_voice == original_stored_voice

  assert updated_voice['name'] == 'integration_new_name'
  assert updated_voice['owner'] == 'me'
  assert updated_voice['type'] == 'instant'
  assert updated_voice['description'] == 'my new description'
  assert updated_voice['gender'] == 'female'
  updated_voice.pop('state')  # stored state is not set to ready immediately after creation
  updated_stored_voice.pop('state')
  assert updated_voice == updated_stored_voice
  with pytest.raises(Exception):
    await api.voice_info(voice_id)


@pytest.mark.asyncio
async def test_get_account_info(api):
  response = await api.account_info()
  assert isinstance(response, dict)
