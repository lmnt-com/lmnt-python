# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Voice"]


class Voice(BaseModel):
    id: str
    """The unique identifier of this voice."""

    name: str
    """The display name of this voice."""

    owner: Literal["system", "me", "other"]
    """The owner of this voice."""

    state: str
    """The state of this voice in the training pipeline (e.g., `ready`, `training`)."""

    description: Optional[str] = None
    """A text description of this voice."""

    gender: Optional[str] = None
    """A tag describing the gender of this voice, e.g. `male`, `female`, `nonbinary`."""

    preview_url: Optional[str] = None
    """A URL that returns a preview speech sample of this voice.

    The file can be played directly in a browser or audio player.
    """

    starred: Optional[bool] = None
    """Whether this voice has been starred by you or not."""

    type: Optional[Literal["instant", "professional"]] = None
    """The method by which this voice was created: `instant` or `professional`."""
