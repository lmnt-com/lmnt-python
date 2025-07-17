# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VoiceUpdateParams"]


class VoiceUpdateParams(TypedDict, total=False):
    description: str
    """A description of this voice."""

    gender: str
    """A tag describing the gender of this voice, e.g. `male`, `female`, `nonbinary`."""

    name: str
    """The display name for this voice."""

    starred: bool
    """If `true`, adds this voice to your starred list."""
