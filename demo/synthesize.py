import argparse
import asyncio
import os
from dotenv import load_dotenv
from lmnt.api import Speech

load_dotenv()  # Don't forget to add your LMNT API key to .env.


async def main(args):
  async with Speech(os.getenv('LMNT_API_KEY')) as s:
    #  Get the list of available voices.
    voices = await s.list_voices()
    print(voices)

    # Get your account information.
    account = await s.account_info()
    print(account)

    # Synthesize text to speech.
    synthesize = await s.synthesize(text=args.text, voice=args.voice, language=args.language)
    with open('output.mp3', 'wb') as f:
      f.write(synthesize['audio'])
    print('Done.')

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Synthesize text to speech using LMNT API')
  parser.add_argument('-t', '--text', required=False, default='This is a test of the LMNT API.', help='Text to synthesize')
  parser.add_argument('-v', '--voice', required=False, default='lily', help='Voice to use')
  parser.add_argument('-l', '--language', required=False, default='en', help='Language code')
  args = parser.parse_args()
  asyncio.run(main(args))
