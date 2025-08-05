from __future__ import annotations

import json
from typing import Any, Dict, List, Final, Union, Literal, Optional

import websockets
from pydantic import Field, BaseModel

URL_STREAMING: Final = "wss://api.lmnt.com/v1/ai/speech/stream"


class Duration(BaseModel):
    """Duration information for a segment of synthesized speech."""
    
    text: str
    start: float = Field(description="Start time in seconds")
    duration: float = Field(description="Duration in seconds")


class AudioMessage(BaseModel):
    """Audio message containing synthesized speech data."""
    
    type: Literal["audio"] = "audio"
    audio: bytes


class ExtrasMessage(BaseModel):
    """Extras message containing metadata about the synthesis."""
    
    type: Literal["extras"] = "extras"
    durations: Optional[List[Duration]] = None
    warning: Optional[str] = None
    buffer_empty: Optional[bool] = None


class ErrorMessage(BaseModel):
    """Error message containing error information."""
    
    type: Literal["error"] = "error"
    error: str


class CompleteMessage(BaseModel):
    """Complete message for commands (reset/flush)."""
    
    type: Literal["complete"] = "complete"
    complete: Literal["reset", "flush"]
    nonce: int


SpeechSessionResponse = Union[AudioMessage, ExtrasMessage, ErrorMessage, CompleteMessage]


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
        self.nonce: int = 0

    async def connect(self) -> None:
        """Establish the websocket connection."""
        self.websocket = await websockets.connect(URL_STREAMING)
        init_msg = {
            "X-API-Key": self.api_key,
            "voice": self.voice,
            "protocol_version": 2,
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

    async def flush(self) -> int:
        """Flush the current text buffer."""
        self.nonce += 1
        await self._send_message({"command": "flush", "nonce": self.nonce})
        return self.nonce

    async def reset(self) -> int:
        """Reset the current text buffer."""
        self.nonce += 1
        await self._send_message({"command": "reset", "nonce": self.nonce})
        return self.nonce

    async def finish(self) -> None:
        """Mark the session as finished."""
        await self._send_message({"command": "eof"})

    async def close(self) -> None:
        """Close the websocket connection."""
        if self.websocket is not None:
            await self.websocket.close()
            self.websocket = None

    async def _send_message(self, message: Dict[str, Any]) -> None:
        """Send a message through the websocket."""
        if self.websocket is not None:
            await self.websocket.send(json.dumps(message))

    def __aiter__(self) -> SpeechSession:
        """Return the async iterator."""
        return self

    async def __anext__(self) -> SpeechSessionResponse:
        """Get the next speech session response."""
        if not self.websocket:
            raise StopAsyncIteration
        try:
            message = await self.websocket.recv()

            if isinstance(message, str):
                return self._parse_text_message(message)
            elif isinstance(message, bytes):
                return AudioMessage(type="audio", audio=message)
            else:
                raise UnexpectedMessageError(f"Unexpected message type: {type(message)}")

        except websockets.exceptions.ConnectionClosed as err:
            raise StopAsyncIteration from err

    def _parse_text_message(self, text_data: str) -> SpeechSessionResponse:
        """Parse a text message from the server."""
        try:
            message_json = json.loads(text_data)
        except json.JSONDecodeError as err:
            raise ValueError(f"Invalid JSON received from server: {text_data}") from err

        if "error" in message_json:
            return ErrorMessage.model_construct(**message_json)
        
        if "complete" in message_json:
            return CompleteMessage.model_construct(**message_json)
        
        if self.return_extras and (
            message_json.get("durations") or message_json.get("warning") or message_json.get("buffer_empty") is not None
        ):
            return ExtrasMessage.model_construct(**message_json)
            
        raise UnexpectedMessageError(f"Unexpected message: {text_data}")
