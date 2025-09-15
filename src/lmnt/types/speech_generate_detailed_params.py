# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SpeechGenerateDetailedParams"]


class SpeechGenerateDetailedParams(TypedDict, total=False):
    text: Required[str]
    """The text to synthesize; max 5000 characters per request (including spaces)."""

    voice: Required[str]
    """
    The voice id of the voice to use; voice ids can be retrieved by calls to
    `List voices` or `Voice info`.
    """

    debug: bool
    """
    When set to true, the generated speech will also be saved to your
    [clip library](https://app.lmnt.com/clips) in the LMNT playground.
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
    """The desired language.

    Two letter ISO 639-1 code. Defaults to auto language detection, but specifying
    the language is recommended for faster generation.
    """

    model: Literal["blizzard"]
    """The model to use for synthesis.

    Learn more about models [here](https://docs.lmnt.com/guides/models).
    """

    return_durations: bool
    """If set as `true`, response will contain a durations object."""

    sample_rate: Literal[8000, 16000, 24000]
    """The desired output sample rate in Hz.

    Defaults to `24000` for all formats except `mulaw` which defaults to `8000`.
    """

    seed: int
    """Seed used to specify a different take; defaults to random"""

    temperature: float
    """Influences how expressive and emotionally varied the speech becomes.

    Lower values (like 0.3) create more neutral, consistent speaking styles. Higher
    values (like 1.0) allow for more dynamic emotional range and speaking styles.
    """

    top_p: float
    """Controls the stability of the generated speech.

    A lower value (like 0.3) produces more consistent, reliable speech. A higher
    value (like 0.9) gives more flexibility in how words are spoken, but might
    occasionally produce unusual intonations or speech patterns.
    """
