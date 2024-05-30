from argparse import ArgumentParser
import asyncio
from dotenv import load_dotenv
from lmnt.api import Speech
from openai import AsyncOpenAI
import os

load_dotenv()  # Don't forget to add your LMNT and OpenAI API keys to .env.

MODEL = 'gpt-3.5-turbo'
DEFAULT_PROMPT = 'Tell me an interesting fact about the universe.'
VOICE_ID = 'lily'


async def reader_task(conn):
  """Streams audio data from the server and writes it to `output.mp3`."""
  with open('output.mp3', 'wb') as f:
    async for msg in conn:
      f.write(msg['audio'])


async def writer_task(conn, prompt):
  """Streams text from ChatGPT to LMNT."""
  client = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'))
  response = await client.chat.completions.create(model=MODEL,
                                                  messages=[{'role': 'user', 'content': prompt}],
                                                  stream=True)

  async for chunk in response:
    if not chunk.choices[0] or not chunk.choices[0].delta or not chunk.choices[0].delta.content:
      continue
    content = chunk.choices[0].delta.content
    await conn.append_text(content)
    print(content, end='', flush=True)

  await conn.finish()


async def main(args):
  speech = Speech(os.getenv('LMNT_API_KEY'))
  conn = await speech.synthesize_streaming(VOICE_ID, return_extras=False, language=args.language)

  t1 = asyncio.create_task(reader_task(conn))
  t2 = asyncio.create_task(writer_task(conn, args.prompt))

  await t1
  await t2
  await speech.close()


if __name__ == '__main__':
  parser = ArgumentParser()
  parser.add_argument('prompt', default=DEFAULT_PROMPT, nargs='?')
  parser.add_argument('-l', '--language', required=False, default='en', help='Language code')
  asyncio.run(main(parser.parse_args()))
