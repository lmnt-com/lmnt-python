import argparse
import asyncio
import os
from dotenv import load_dotenv
from lmnt.api import Speech

load_dotenv()  # Don't forget to add your LMNT API key to .env.


async def main(args):
  async with Speech(os.getenv('LMNT_API_KEY')) as speech:
    # Get the list of available voices.
    voices = await speech.list_voices()
    print(voices)

    # Create a voice. Once completed, it will be available in your list of voices.
    create_voice = await speech.create_voice('Demo voice', True, args.input_files)
    print(create_voice)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Create a voice using LMNT API')
  parser.add_argument('-i', '--input_files', nargs='+', required=False, default=['sample-audio-input.mp3'], help='Input file path')
  args = parser.parse_args()
  asyncio.run(main(args))
