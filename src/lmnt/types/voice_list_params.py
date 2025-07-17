# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VoiceListParams"]


class VoiceListParams(TypedDict, total=False):
    owner: str
    """Which owner's voices to return. Choose from `system`, `me`, or `all`."""

    starred: str
    """If true, only returns voices that you have starred."""
