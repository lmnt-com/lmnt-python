# LMNT Python Library
The LMNT Python library provides convenient access to the LMNT API from applications written in the Python language.

[[Documentation]](https://docs.lmnt.com/sdk/python/introduction)

## Installation
Installing from PyPI is the quickest way to get started:

```sh
pip install --upgrade lmnt
```

Install from source with:

```sh
python setup.py install
```

## Getting started

The most common operation you'll perform is a `synthesize` request. Given some text and a voice, it will return an audio
file that you can play back. Take a look at our [documentation](https://docs.lmnt.com/sdk/python/introduction) for a deeper dive into the SDK.

```python
from lmnt.api import Speech

LMNT_API_KEY = ...  # fill in your API key here

async with Speech(LMNT_API_KEY) as speech:
  synthesis = await speech.synthesize('Hello, world.', voice='4e95c4a7-95aa-4b1d-bc23-00f7d1d484ea', format='wav')
  with open('output.wav', 'wb') as f:
    f.write(synthesis['audio'])
```

## More examples

You can find more examples in the [demo](demo) directory.

## License
[Apache 2.0](LICENSE)
