# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["SpeechConvertParams"]


class SpeechConvertParams(TypedDict, total=False):
    audio: Required[FileTypes]
    """The audio file to be converted into a new voice.

    Specify source language using the `language` parameter. Acceptable formats:
    `wav`, `mp3`. Max file size: 1 MB.
    """

    voice: Required[str]
    """The voice id to convert the speech into.

    Voice ids can be retrieved by calls to `List voices` or `Voice info`.
    """

    format: Literal["aac", "mp3", "ulaw", "wav", "webm", "pcm_s16le", "pcm_f32le"]
    """The desired output format of the audio.

    If you are using a streaming endpoint, you'll generate audio faster by selecting
    a streamable format since chunks are encoded and returned as they're generated.
    For non-streamable formats, the entire audio will be synthesized before
    encoding.

    Streamable formats:

    - `mp3`: 96kbps MP3 audio.
    - `ulaw`: 8-bit G711 µ-law audio with a WAV header.
    - `webm`: WebM format with Opus audio codec.
    - `pcm_s16le`: PCM signed 16-bit little-endian audio.
    - `pcm_f32le`: PCM 32-bit floating-point little-endian audio.

    Non-streamable formats:

    - `aac`: AAC audio codec.
    - `wav`: 16-bit PCM audio in WAV container.
    """

    language: Literal[
        "auto",
        "ar",
        "de",
        "en",
        "es",
        "fr",
        "hi",
        "id",
        "it",
        "ja",
        "ko",
        "nl",
        "pl",
        "pt",
        "ru",
        "sv",
        "th",
        "tr",
        "uk",
        "ur",
        "vi",
        "zh",
    ]
    """The language of the source audio. Two letter ISO 639-1 code."""

    sample_rate: Literal[8000, 16000, 24000]
    """The desired output sample rate in Hz.

    Defaults to `24000` for all formats except `mulaw` which defaults to `8000`.
    """
