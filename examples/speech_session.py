import asyncio

from lmnt import AsyncLmnt
from lmnt.resources.sessions import SpeechSession


async def main() -> None:
    # Gets API Key from environment variable LMNT_API_KEY
    lmnt = AsyncLmnt()

    # Construct the streaming connection with our desired voice
    session = await lmnt.speech.sessions.create(voice="leah")
    write_task = asyncio.create_task(write_messages(session))
    read_task = asyncio.create_task(read_messages(session))

    await asyncio.gather(write_task, read_task)


async def write_messages(session: SpeechSession) -> None:
    # Simulate a message stream w/ a 1 second delay between messages
    for i in range(5):
        await session.append_text("Hello, world!")
        print(f" ** Sent to LMNT -- Message {i} ** ")
        await asyncio.sleep(1)

    # After finish is called, the server will flush its buffer and close the
    # connection once all the audio has been synthesized
    await session.finish()


async def read_messages(session: SpeechSession) -> None:
    with open("stream-output.mp3", "wb") as audio_file:
        async for message in session:
            if message.type == "audio":
                audio_bytes = len(message.audio)
                print(f" ** Received from LMNT -- {audio_bytes} bytes ** ")
                audio_file.write(message.audio)


if __name__ == "__main__":
    asyncio.run(main())
