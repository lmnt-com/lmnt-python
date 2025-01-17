import asyncio
import os
import yaml
import whisper

from lmnt.api import Speech
from typing import Optional
from openai import AsyncOpenAI
from mistralai import Mistral


class LMNTStream:
  """
  Handles LMNT API for text-to-speech streaming.
  """

  def __init__(self, api_key: Optional[str] = None, model: str = 'blizzard', voice_id: str = 'lily'):
    """
    Initialize the LMNTHandler.
    Args:
        api_key (str): The LMNT API key. Defaults to the LMNT_API_KEY environment variable.
        voice_id (str): The ID of the voice to use for LMNT TTS.
        output_file (str): File to save the audio output.
    """
    self.api_key = api_key or os.environ.get('LMNT_API_KEY')
    self.voice_id = voice_id
    self.model = model
    self.output_file = 'output.mp3'

  async def __call__(self, text_stream):
    """
    Streams text to LMNT API and saves audio output.
    Args:
        text_stream (async generator): Stream of text chunks to send to LMNT.
    """
    async with Speech(self.api_key) as speech:
      connection = await speech.synthesize_streaming(self.voice_id)
      reader_task = asyncio.create_task(self._reader_task(connection))
      writer_task = asyncio.create_task(self._writer_task(connection, text_stream))
      await asyncio.gather(reader_task, writer_task)

  async def _reader_task(self, connection):
    """Reads audio data from LMNT and writes to a file."""
    with open(self.output_file, 'wb') as f:
      async for message in connection:
        f.write(message['audio'])

  async def _writer_task(self, connection, text_stream):
    """Streams text to LMNT."""
    async for text in text_stream:
      await connection.append_text(text)
    await connection.flush()


class LMNTtts:
  def __init__(self, api_key: Optional[str] = None, model: str = 'blizzard', voice_id: str = 'lily'):
    """
    Initialize the LMNTHandler.
    Args:
        api_key (str): The LMNT API key. Defaults to the LMNT_API_KEY environment variable.
        voice_id (str): The ID of the voice to use for LMNT TTS.
        output_file (str): File to save the audio output.
    """
    self.api_key = api_key or os.environ.get('LMNT_API_KEY')
    self.voice_id = voice_id
    self.model = model
    self.output_file = 'output.mp3'

  async def synthesize(self, text):
    """
    Synthesize text using the LMNT API.
    Args:
        text (str): The text to synthesize.
    Returns:
        bytes: The synthesized audio.
    """
    async with Speech(self.api_key) as speech:
      synthesis = await speech.synthesize(text, self.voice_id, model=self.model)
    with open(self.output_file, 'wb') as f:
      f.write(synthesis['audio'])


class MistralStream:
  """
  Handles text generation using  Mistral
  """

  def __init__(self, api_key: Optional[str] = None, model: str = 'mistral-tiny', prompt: str = ''):
    """
    Initialize the LLMHandler.
    Args:
        model (str): The LLM model to use.
        prompt (str): The default text generation prompt.
    """
    self.api_key = api_key or os.environ.get('MISTRAL_API_KEY')
    self.model = model
    self._set_prompt(prompt)

  def _set_prompt(self, prompt: str = ''):
    """Set the text generation prompt."""
    if prompt:
      with Mistral(api_key=self.api_key) as client:
        chat_response = client.chat.complete(
            model=self.model,
            messages=[{'role': 'system', 'content': prompt}],
        )
      print(chat_response.choices[0].message.content)

  async def __call__(self, query_text: str):
    """
    Generates text from the LLM and streams it as chunks.
    Returns:
        async generator: Stream of text chunks.
    """
    with Mistral(api_key=self.api_key) as client:
      response = await client.chat.stream_async(
          model=self.model,
          messages=[{'role': 'user', 'content': query_text}],
      )
    async for chunk in response:
      if chunk.data.choices[0].delta.content is not None:
        yield chunk.data.choices[0].delta.content


class OpenAIStream:
  """
  Handles text generation using an LLM (e.g., OpenAI GPT).
  """

  def __init__(self, api_key=None, model='gpt-3.5-turbo', prompt=None):
    """
    Initialize the LLMHandler.
    Args:
        model (str): The LLM model to use.
        prompt (str): The default text generation prompt.
    """
    self.api_key = api_key or os.environ.get('OPENAI_API_KEY')
    self.model = model
    self.client = AsyncOpenAI(api_key=api_key)
    self._set_prompt(prompt)

  def _set_prompt(self, prompt=None):
    """Set the text generation prompt."""
    if prompt is not None:
      chat_response = self.client.chat.complete(
          model=self.model,
          messages=[{'role': 'system', 'content': prompt}],
      )
    print(chat_response.choices[0].message.content)

  async def __call__(self, query_text):
    """
    Generates text from the LLM and streams it as chunks.
    Returns:
        async generator: Stream of text chunks.
    """
    response = await self.client.chat.completions.create(
        model=self.model,
        messages=[{'role': 'user', 'content': self.prompt}],
        stream=True,
    )

    async for chunk in response:
      if (
          chunk.choices
          and chunk.choices[0].delta
          and chunk.choices[0].delta.content
      ):
        yield chunk.choices[0].delta.content


class LMNTAgent:
  def __init__(self, config_path: Optional[str] = None):
    """
    Initialize the LMNTAgent with a configuration file.
    Args:
        config (dict): Configuration dictionary.
    """
    if config_path is None:
      config_path = 'config.yaml'
    with open(config_path, 'r') as f:
      config = yaml.safe_load(f)

    self.config = config
    self._whisper = None
    self._llm = None
    self._init_lmnt()
    self._init_whisper()
    self._init_llm()

  def _init_lmnt(self):
    """Initialize the LMNT API handler."""
    lmnt_config = self.config['lmnt_api']
    api_key = lmnt_config.get('api_key', None)
    model = lmnt_config.get('model', 'blizzard')
    voice = lmnt_config.get('voice', 'lily')
    self.lmnt_stream = LMNTStream(api_key, model, voice)

  def _init_whisper(self):
    """Initialize the Whisper transcription handler."""
    whisper_config = self.config.get('whisper', {})
    if not whisper_config.get('enabled', False):
      self._whisper = None
      return
    model = whisper_config.get('model')
    self._whisper = whisper.load_model(model)

  def _init_llm(self):
    """Initialize the LLM handler."""
    llm_config = self.config.get('llm', {})
    if not llm_config.get('enabled', False):
      self._llm = None
      return
    model = llm_config['model']
    api_key = llm_config.get('api_key', None)
    prompt = llm_config.get('prompt', None)
    self._llm = MistralStream(api_key, model, prompt)

  def transcribe_audio(self, audio_bytes: bytes) -> str:
    """
    Transcribe audio bytes using the Whisper API.
    Args:
        audio_bytes (bytes):
    Returns
        str: Transcribed text.
    """
    assert self._whisper is not None, 'Whisper mode is not enabled.'
    return self._whisper.transcribe(audio_bytes)

  async def run(self, input_data: str | bytes):
    """
    Run the agent based on the detected mode.
    Args:
        input_data: Input data (text or audio bytes).
    """

    # Transcribe audio if input is bytes
    if isinstance(input_data, bytes):
      try:
        text = self.transcribe_audio(input_data)
        print(f'Transcribed text: {text}')
      except Exception as e:
        print(f'Error transcribing audio: {e}')
        return
    else:
      text = input_data

    # Process text with LLM if enabled
    if self._llm:
      try:
        text = self._llm(text)
      except Exception as e:
        print(f'Error processing text: {e}')
        return

    # Synthesize audio
    try:
      await self.lmnt_stream(text)
    except Exception as e:
      print(f'Error synthesizing audio: {e}')
      return


# Example Usage
if __name__ == '__main__':
  import argparse
  import yaml

  parser = argparse.ArgumentParser()
  parser.add_argument('--config', type=str, default='config.yaml', help='Path to configuration file.')
  args = parser.parse_args()

  agent = LMNTAgent(args.config)
  input_data = 'Give me a list of the best restuarants in Berlin?'
  asyncio.run(agent.run(input_data))
