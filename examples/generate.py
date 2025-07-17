from lmnt import Lmnt

client = Lmnt()

# Use streaming response to get chunks as they arrive
with client.speech.with_streaming_response.generate(
    text="""Okay that's the 4-piece Original Combo with coleslaw and iced tea, and the two-pack of Nashville Hot sliders. Before I get you the total, uh, have you tried our new Peach Cobbler? It's warm, got a buttery crust, folks are loving it - only $2.99 extra.""",
    voice="leah",
) as response:
    # Collect all chunks and print when each arrives
    all_content = b""
    chunk_count = 0

    for chunk in response.iter_bytes():
        chunk_count += 1
        print(f"Chunk {chunk_count} received: {len(chunk)} bytes")
        all_content += chunk

    print(f"Total chunks received: {chunk_count}")
    print(f"Total content size: {len(all_content)} bytes")

# Write the complete audio to file
with open("output.wav", "wb") as f:
    f.write(all_content)

print("Audio saved to output.wav")
