# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SpeechGenerateDetailedResponse", "Duration"]


class Duration(BaseModel):
    duration: float
    """The spoken duration of each synthesized input element, in seconds."""

    start: float
    """The start time of each synthsized input element, in seconds."""

    text: str
    """The synthesized input elements; beginning and ending with a short silence."""


class SpeechGenerateDetailedResponse(BaseModel):
    audio: str
    """
    The base64-encoded audio file; the format is determined by the `format`
    parameter.
    """

    seed: int
    """
    The seed used to generate this speech; can be used to replicate this output take
    (assuming the same text is resynthsized with this seed number,
    [see here](http://docs.lmnt.com/speech/seed) for more details).
    """

    durations: Optional[List[Duration]] = None
    """
    A JSON object outlining the spoken duration of each synthesized input element
    (words and non-words like spaces, punctuation, etc.). See an
    [example of this object](https://imgur.com/Uw6qNzY.png) for the input string
    "Hello world!"
    """
