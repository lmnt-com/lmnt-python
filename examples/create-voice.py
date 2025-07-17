from pathlib import Path

from lmnt import Lmnt

client = Lmnt()

response = client.voices.create(
    name="My Voice",
    files=[Path("sample1.wav"), Path("sample2.wav")],
    enhance=False,
)

print(response)
