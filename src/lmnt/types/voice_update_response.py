# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .voice import Voice
from .._models import BaseModel

__all__ = ["VoiceUpdateResponse"]


class VoiceUpdateResponse(BaseModel):
    voice: Voice
    """Voice details"""
