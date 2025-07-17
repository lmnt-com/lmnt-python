# Speech

Types:

```python
from lmnt.types import SpeechGenerateDetailedResponse
```

Methods:

- <code title="post /v1/ai/speech/convert">client.speech.<a href="./src/lmnt/resources/speech.py">convert</a>(\*\*<a href="src/lmnt/types/speech_convert_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /v1/ai/speech/bytes">client.speech.<a href="./src/lmnt/resources/speech.py">generate</a>(\*\*<a href="src/lmnt/types/speech_generate_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /v1/ai/speech">client.speech.<a href="./src/lmnt/resources/speech.py">generate_detailed</a>(\*\*<a href="src/lmnt/types/speech_generate_detailed_params.py">params</a>) -> <a href="./src/lmnt/types/speech_generate_detailed_response.py">SpeechGenerateDetailedResponse</a></code>

# Accounts

Types:

```python
from lmnt.types import AccountRetrieveResponse
```

Methods:

- <code title="get /v1/account">client.accounts.<a href="./src/lmnt/resources/accounts.py">retrieve</a>() -> <a href="./src/lmnt/types/account_retrieve_response.py">AccountRetrieveResponse</a></code>

# Voices

Types:

```python
from lmnt.types import Voice, VoiceUpdateResponse, VoiceListResponse, VoiceDeleteResponse
```

Methods:

- <code title="post /v1/ai/voice">client.voices.<a href="./src/lmnt/resources/voices.py">create</a>(\*\*<a href="src/lmnt/types/voice_create_params.py">params</a>) -> <a href="./src/lmnt/types/voice.py">Voice</a></code>
- <code title="get /v1/ai/voice/{id}">client.voices.<a href="./src/lmnt/resources/voices.py">retrieve</a>(id) -> <a href="./src/lmnt/types/voice.py">Voice</a></code>
- <code title="put /v1/ai/voice/{id}">client.voices.<a href="./src/lmnt/resources/voices.py">update</a>(id, \*\*<a href="src/lmnt/types/voice_update_params.py">params</a>) -> <a href="./src/lmnt/types/voice_update_response.py">VoiceUpdateResponse</a></code>
- <code title="get /v1/ai/voice/list">client.voices.<a href="./src/lmnt/resources/voices.py">list</a>(\*\*<a href="src/lmnt/types/voice_list_params.py">params</a>) -> <a href="./src/lmnt/types/voice_list_response.py">VoiceListResponse</a></code>
- <code title="delete /v1/ai/voice/{id}">client.voices.<a href="./src/lmnt/resources/voices.py">delete</a>(id) -> <a href="./src/lmnt/types/voice_delete_response.py">VoiceDeleteResponse</a></code>
