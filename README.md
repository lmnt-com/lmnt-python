# LMNT Python SDK

[![PyPI version](https://img.shields.io/pypi/v/lmnt.svg?label=pypi%20(stable))](https://pypi.org/project/lmnt/)

The LMNT Python SDK provides convenient access to the LMNT API from Python applications.

## Documentation

Full documentation is available at [docs.lmnt.com/api/sdks/python](https://docs.lmnt.com/api/sdks/python).

## Installation

```sh
pip install lmnt
```

## Getting started

```python
import os
from lmnt import Lmnt

client = Lmnt(
    api_key=os.environ.get("LMNT_API_KEY"),  # This is the default and can be omitted
)

response = client.speech.generate(
    text="hello world.",
    voice="leah",
)
```

## Requirements

Python 3.10 or higher.

## Contributing

See [the contributing documentation](./CONTRIBUTING.md).
