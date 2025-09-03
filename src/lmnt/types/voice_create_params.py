# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes, SequenceNotStr

__all__ = ["VoiceCreateParams"]


class VoiceCreateParams(TypedDict, total=False):
    enhance: Required[bool]
    """
    For unclean audio with background noise, applies processing to attempt to
    improve quality. Default is `false` as this can also degrade quality in some
    circumstances.
    """

    files: Required[SequenceNotStr[FileTypes]]
    """
    One or more input audio files to train the voice in the form of binary `wav`,
    `mp3`, `mp4`, `m4a`, or `webm` attachments.

    - Max attached files: 20.
    - Max total file size: 250 MB.
    """

    name: Required[str]
    """The display name for this voice"""

    description: str
    """A text description of this voice."""

    gender: str
    """A tag describing the gender of this voice. Has no effect on voice creation."""
