# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AccountRetrieveResponse", "Plan", "Usage"]


class Plan(BaseModel):
    character_limit: int
    """The number of characters you are allowed to synthesize in this billing period."""

    commercial_use_allowed: bool

    professional_voice_limit: Optional[int] = None
    """The number of professional voices you are allowed to create."""

    type: str
    """The type of plan you are subscribed to."""

    instant_voice_limit: Optional[int] = None
    """The number of instant voices you are allowed to create."""


class Usage(BaseModel):
    characters: int
    """The number of characters you have synthesized in this billing period."""

    professional_voices: int
    """The number of professional voices you have created."""

    instant_voices: Optional[int] = None
    """The number of instant voices you have created."""


class AccountRetrieveResponse(BaseModel):
    plan: Plan

    usage: Usage
