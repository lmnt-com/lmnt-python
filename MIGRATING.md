# Migrating from v1 to v2

This guide helps you migrate from the legacy v1 SDK to the new v2 SDK. The new SDK provides more streaming functionality, a more modern, type-safe interface with better error handling, and improved performance.

## Installation

```bash
# Remove the old SDK
pip uninstall lmnt

# Install the new SDK
pip install lmnt
```

## Key Changes

### Client Initialization

```python
# Old SDK (v1)
import asyncio
from lmnt.api import Speech

async def main():
    async with Speech('your-api-key') as speech:
        # Use speech client
        pass

# New SDK (v2)
from lmnt import Lmnt, AsyncLmnt

# Synchronous client
client = Lmnt()  # Uses LMNT_API_KEY environment variable

# Async client
async def main():
    client = AsyncLmnt()  # Uses LMNT_API_KEY environment variable
    # Use client
```

### Speech Synthesis

```python
# Old SDK
async with Speech('your-api-key') as speech:
    result = await speech.synthesize('Hello world', 'voice-id')
    # result: {'audio': bytes, 'durations': [...], 'seed': 123}
    with open('output.mp3', 'wb') as f:
        f.write(result['audio'])

# New SDK - Synchronous
client = Lmnt()
response = client.speech.generate(
    text='Hello world',
    voice='voice-id',
)
# response: BinaryAPIResponse
with open('output.mp3', 'wb') as f:
    f.write(response.read())

# New SDK - Async
async def main():
    client = AsyncLmnt()
    response = await client.speech.generate(
        text='Hello world',
        voice='voice-id',
    )
    # response: AsyncBinaryAPIResponse
    with open('output.mp3', 'wb') as f:
        f.write(await response.read())
```

### Streaming Speech Synthesis

```python
# Old SDK
async with Speech('your-api-key') as speech:
    conn = await speech.synthesize_streaming('voice-id', return_extras=True)
    await conn.append_text('Hello world')
    await conn.finish()
    
    async for chunk in conn:
        # chunk: {'audio': bytes, 'durations': [...], 'warning': '...'}
        print(f"Received {len(chunk['audio'])} bytes")

# New SDK - WebSocket Sessions
async def main():
    client = AsyncLmnt()
    session = await client.speech.sessions.create(
        voice='voice-id',
        return_extras=True
    )
    
    await session.append_text('Hello world')
    await session.finish()
    
    async for message in session:
        # message: SpeechSessionResponse
        print(f"Received {len(message.audio)} bytes")
        if message.durations:
            print(f"Durations: {message.durations}")

# New SDK - HTTP Streaming
client = Lmnt()
with client.speech.with_streaming_response.generate(
    text='Hello world',
    voice='voice-id',
) as response:
    for chunk in response.iter_bytes():
        print(f"Received {len(chunk)} bytes")
```

### Voice Management

```python
# Old SDK
async with Speech('your-api-key') as speech:
    voices = await speech.list_voices(starred=True)
    voice = await speech.voice_info('voice-id')
    await speech.update_voice('voice-id', name='New Name')
    await speech.delete_voice('voice-id')
    await speech.create_voice('voice-name', False, ['file1.wav', 'file2.wav'])

# New SDK - Synchronous
client = Lmnt()
voices = client.voices.list(starred=True)
voice = client.voices.retrieve('voice-id')
client.voices.update('voice-id', name='New Name')
client.voices.delete('voice-id')
client.voices.create(
    name='voice-name',
    enhance=False,
    files=[Path('file1.wav'), Path('file2.wav')]
)

# New SDK - Async
async def main():
    client = AsyncLmnt()
    voices = await client.voices.list(starred=True)
    voice = await client.voices.retrieve('voice-id')
    await client.voices.update('voice-id', name='New Name')
    await client.voices.delete('voice-id')
    await client.voices.create(
        name='voice-name',
        enhance=False,
        files=[Path('file1.wav'), Path('file2.wav')]
    )
```

### Account Information

```python
# Old SDK
async with Speech('your-api-key') as speech:
    account = await speech.account_info()

# New SDK
client = Lmnt()
account = client.accounts.retrieve()
```

### Error Handling

```python
# Old SDK
from lmnt.api import SpeechError

try:
    async with Speech('your-api-key') as speech:
        result = await speech.synthesize('Hello', 'invalid-voice')
except SpeechError as e:
    print(f"Error: {e.message}")

# New SDK
from lmnt import NotFoundError, AuthenticationError, APIError

try:
    client = Lmnt()
    response = client.speech.generate(text='Hello', voice='invalid-voice')
except NotFoundError as e:
    print(f"Voice not found: {e}")
except AuthenticationError as e:
    print(f"Authentication failed: {e}")
except APIError as e:
    print(f"API error: {e}")
```

## Advanced Features

### Response Streaming

```python
# New SDK - Stream to file
client = Lmnt()
with client.speech.with_streaming_response.generate(
    text='Long text here...',
    voice='voice-id'
) as response:
    response.stream_to_file('output.mp3')

# Async version
async def main():
    client = AsyncLmnt()
    async with client.speech.with_streaming_response.generate(
        text='Long text here...',
        voice='voice-id'
    ) as response:
        await response.stream_to_file('output.mp3')
```

### Raw Response Access

```python
# New SDK - Access raw HTTP response
client = Lmnt()
response = client.with_raw_response.speech.generate(
    text='Hello world',
    voice='voice-id'
)
print(f"Status: {response.status_code}")
print(f"Headers: {response.headers}")
audio_data = response.read()
```

### Custom Configuration

```python
# New SDK - Custom client configuration - Use AioHttp client for improved performance
from lmnt import DefaultAioHttpClient
from lmnt import AsyncLmnt

async with AsyncLmnt(
    api_key='your-api-key',
    base_url='https://api.lmnt.com',
    timeout=30.0,
    max_retries=3,
    http_client=DefaultAioHttpClient()
) as client:
```

## Migration Checklist

- [ ] Update import statements
- [ ] Replace `Speech` class with `Lmnt` or `AsyncLmnt`
- [ ] Update method calls to use new resource-based API
- [ ] Handle response objects instead of dictionaries
- [ ] Update error handling to use specific exception types
- [ ] Test streaming functionality with new session API
- [ ] Update file handling to use `Path` objects
- [ ] Remove context manager usage if not needed

## Need Help?

If you encounter issues during migration, please:
1. Check the [API documentation](https://docs.lmnt.com)
2. Review the [examples](examples/) in the new SDK
3. Open an issue on the [GitHub repository](https://github.com/lmnt-python)
