import json
from typing import Any, Dict, List, Final, Optional
from dataclasses import dataclass

import websockets
from websockets.typing import Data

URL_STREAMING: Final = "wss://api.lmnt.com/v1/ai/speech/stream"


@dataclass
class Duration:
    """Duration information for a segment of synthesized speech."""

    text: str
    start: float  # Start time in seconds
    duration: float  # Duration in seconds


@dataclass
class SpeechSessionResponse:
    """Response from a speech session connection."""

    audio: bytes
    durations: Optional[List[Duration]] = None
    warning: Optional[str] = None
    buffer_empty: Optional[bool] = None


class UnexpectedMessageError(Exception):
    """Exception raised when an unexpected message is received from the server."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(f"Unexpected message received from server: {message}")


class SpeechSession:
    """Async websocket connection for LMNT speech session."""

    def __init__(
        self,
        api_key: str,
        voice: str,
        format: Optional[str] = None,
        language: Optional[str] = None,
        sample_rate: Optional[int] = None,
        return_extras: Optional[bool] = None,
    ):
        self.api_key = api_key
        self.voice = voice
        self.format = format
        self.language = language
        self.sample_rate = sample_rate
        self.return_extras = return_extras
        self.websocket: Optional[Any] = None

    async def connect(self) -> None:
        """Establish the websocket connection."""
        self.websocket = await websockets.connect(URL_STREAMING)
        init_msg = {
            "X-API-Key": self.api_key,
            "voice": self.voice,
        }
        if self.format:
            init_msg["format"] = self.format
        if self.language:
            init_msg["language"] = self.language
        if self.sample_rate:
            init_msg["sample_rate"] = str(self.sample_rate)
        if self.return_extras:
            init_msg["return_extras"] = str(self.return_extras)
        if self.websocket is not None:
            await self.websocket.send(json.dumps(init_msg))

    async def append_text(self, text: str) -> None:
        """Append text to be synthesized."""
        await self._send_message({"text": text})

    async def flush(self) -> None:
        """Flush the current text buffer."""
        await self._send_message({"flush": True})

    async def finish(self) -> None:
        """Mark the session as finished."""
        await self._send_message({"eof": True})

    async def close(self) -> None:
        """Close the websocket connection."""
        if self.websocket is not None:
            await self.websocket.close()
            self.websocket = None

    async def _send_message(self, message: Dict[str, Any]) -> None:
        """Send a message through the websocket."""
        if self.websocket is not None:
            await self.websocket.send(json.dumps(message))

    def __aiter__(self) -> "SpeechSession":
        """Return the async iterator."""
        return self

    async def __anext__(self) -> SpeechSessionResponse:
        """Get the next speech session response."""
        if not self.websocket:
            raise StopAsyncIteration
        try:
            if self.return_extras:
                extras_message = await self.websocket.recv()
                if not isinstance(extras_message, str):
                    raise UnexpectedMessageError("Expected string for extras message")
                extras = self._parse_and_check_error(extras_message)
                audio_msg = await self.websocket.recv()
                audio_data = self._process_audio_data(audio_msg)
                durations = None
                if extras.get("durations"):
                    durations = [Duration(**d) for d in extras["durations"]]
                return SpeechSessionResponse(
                    audio=audio_data,
                    durations=durations,
                    warning=extras.get("warning"),
                    buffer_empty=extras.get("buffer_empty"),
                )
            else:
                audio_msg = await self.websocket.recv()
                audio_data = self._process_audio_data(audio_msg)
                return SpeechSessionResponse(audio=audio_data)
        except websockets.exceptions.ConnectionClosed as err:
            raise StopAsyncIteration from err

    def _process_audio_data(self, audio_msg: Data) -> bytes:
        """Process the audio data. Handles binary audio data and JSON error messages."""
        if isinstance(audio_msg, bytes):
            return audio_msg
        else:
            self._parse_and_check_error(str(audio_msg))
        raise UnexpectedMessageError(str(audio_msg))

    def _parse_and_check_error(self, message: str) -> Dict[str, Any]:
        """JSON parse a message and check for errors."""
        try:
            msg_json: Dict[str, Any] = json.loads(message)
        except json.JSONDecodeError as err:
            raise ValueError(f"Invalid JSON received from server: {message}") from err
        if "error" in msg_json:
            raise ValueError(msg_json["error"])
        return msg_json
