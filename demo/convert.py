import argparse
import asyncio
from lmnt.api import Speech


async def main(args):
  async with Speech() as s:
    with open(args.audio, 'rb') as f:
      audio = f.read()

    converted_audio = await s.convert(audio=audio, voice=args.voice)
    with open('output.mp3', 'wb') as f:
      f.write(converted_audio)
    print('Done.')


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Convert speech to a different voice')
  parser.add_argument('-a', '--audio', required=True, help='Filename of audio to convert')
  parser.add_argument('-v', '--voice', required=True, help='Voice to use')
  args = parser.parse_args()
  asyncio.run(main(args))
