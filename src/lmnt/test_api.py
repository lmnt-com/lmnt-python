import pytest
from api import Speech

X_API_KEY = ""
STAGING_URL = 'https://api.staging.lmnt.com'
PROD_URL = 'https://api.lmnt.com'

@pytest.fixture
async def api():
    async with Speech(X_API_KEY, _BASE_URL=STAGING_URL) as speech:
        yield speech

@pytest.mark.asyncio
async def test_init(api):
    assert api is not None

@pytest.mark.asyncio
async def test_list_voices(api):
    voices = await api.list_voices()
    assert isinstance(voices, dict)
    assert len(voices) > 0

@pytest.mark.asyncio
async def test_synthesize_streaming(api):
    voice = 'shanti'
    result = await api.synthesize_streaming(voice)
    assert result is not None

@pytest.mark.asyncio
async def test_durations(api):
    voice = 'shanti'
    text = 'Example Text'
    result = await api.synthesize(text=text, voice=voice, durations=True)
    assert result is not None
    assert 'durations' in result
    assert 'phonemes' not in result
    assert 'audio' in result
    assert len(result['durations']) > 0
    assert len(result['audio']) > 0

@pytest.mark.asyncio
async def test_synthesize_with_invalid_voice(api):
    voice = 'invalid_voice'
    text = 'Example Text'
    with pytest.raises(Exception):
        await api.synthesize(text=text, voice=voice)

@pytest.mark.asyncio
async def test_synthesize_with_empty_text(api):
    voice = 'shanti'
    text = ''
    with pytest.raises(Exception):
        await api.synthesize(text=text, voice=voice)
