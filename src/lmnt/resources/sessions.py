from typing import Literal, Optional

from .._resource import AsyncAPIResource
from ..lib.websocket_streaming import SpeechSession

__all__ = ["AsyncSessionsResource", "SpeechSession"]


class AsyncSessionsResource(AsyncAPIResource):
    """Methods for the Sessions resource."""

    async def create(
        self,
        *,
        voice: str,
        format: Optional[Literal["mp3", "raw", "ulaw", "webm"]] = None,
        language: Optional[str] = None,
        sample_rate: Optional[Literal[8000, 16000, 24000]] = None,
        return_extras: Optional[bool] = None,
    ) -> SpeechSession:
        """Create a new websocket connection for full-duplex streaming speech synthesis.
        The websocket connection is cleanly closed when the user calls finish().

        Args:
            voice: The voice id of the voice to use for synthesis
            format: The file format of the synthesized audio output ('mp3', 'raw', 'ulaw', 'webm')
            language: The desired language of the synthesized speech. Two letter ISO 639-1 code.
            sample_rate: The desired output sample rate in Hz (8000, 16000, or 24000)
            return_extras: If True, response will contain a durations object.

        Returns:
            SpeechSession: A new streaming speech session
        """
        session = SpeechSession(
            self._client.api_key,
            voice=voice,
            format=format,
            language=language,
            sample_rate=sample_rate,
            return_extras=return_extras,
        )
        await session.connect()
        return session
