import asyncio
import openai
import os
from dotenv import load_dotenv
from argparse import ArgumentParser
from lmnt.api import Speech

load_dotenv()  # Don't forget to add your LMNT and OpenAI API keys to .env.
openai.api_key = os.getenv('OPENAI_API_KEY')

MODEL = 'gpt-3.5-turbo'
DEFAULT_PROMPT = 'Tell me an interesting fact about the universe.'


async def reader_task(conn):
  """Streams audio data from the server and writes it to `output.mp3`."""
  with open('output.mp3', 'wb') as f:
    async for msg in conn:
      f.write(msg['audio'])


async def writer_task(conn, prompt):
  """Streams text from ChatGPT to LMNT."""
  response = await openai.ChatCompletion.acreate(
      model=MODEL,
      messages=[{'role': 'user', 'content': prompt}],
      temperature=0,
      stream=True
  )

  async for chunk in response:
    if 'choices' not in chunk:
      continue
    choice = chunk['choices'][0]
    if 'delta' not in choice or 'content' not in choice['delta']:
      continue

    await conn.append_text(choice['delta']['content'])
    print(choice['delta']['content'], end='', flush=True)

  await conn.finish()


async def main(args):
  s = Speech(os.getenv('LMNT_API_KEY'))
  conn = await s.synthesize_streaming('mrnmrz72', return_extras=False)

  t1 = asyncio.create_task(reader_task(conn))
  t2 = asyncio.create_task(writer_task(conn, args.prompt))

  await t1
  await t2
  await s.close()


if __name__ == '__main__':
  parser = ArgumentParser()
  parser.add_argument('prompt', default=DEFAULT_PROMPT, nargs='?')
  asyncio.run(main(parser.parse_args()))
