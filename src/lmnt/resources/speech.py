# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

import httpx

from ..types import speech_convert_params, speech_generate_params, speech_generate_detailed_params
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .sessions import AsyncSessionsResource
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.speech_generate_detailed_response import SpeechGenerateDetailedResponse

__all__ = ["SpeechResource", "AsyncSpeechResource"]


class SpeechResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpeechResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lmnt-com/lmnt-python#accessing-raw-response-data-eg-headers
        """
        return SpeechResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpeechResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lmnt-com/lmnt-python#with_streaming_response
        """
        return SpeechResourceWithStreamingResponse(self)

    def convert(
        self,
        *,
        audio: FileTypes,
        voice: str,
        format: Literal["aac", "mp3", "ulaw", "wav", "webm", "pcm_s16le", "pcm_f32le"] | Omit = omit,
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
        | Omit = omit,
        sample_rate: Literal[8000, 16000, 24000] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Converts speech from one voice to another.

        Args:
          audio: The audio file to be converted into a new voice. Specify source language using
              the `language` parameter. Acceptable formats: `wav`, `mp3`. Max file size: 1 MB.

          voice: The voice id to convert the speech into. Voice ids can be retrieved by calls to
              `List voices` or `Voice info`.

          format: The desired output format of the audio. If you are using a streaming endpoint,
              you'll generate audio faster by selecting a streamable format since chunks are
              encoded and returned as they're generated. For non-streamable formats, the
              entire audio will be synthesized before encoding.

              Streamable formats:

              - `mp3`: 96kbps MP3 audio.
              - `ulaw`: 8-bit G711 µ-law audio with a WAV header.
              - `webm`: WebM format with Opus audio codec.
              - `pcm_s16le`: PCM signed 16-bit little-endian audio.
              - `pcm_f32le`: PCM 32-bit floating-point little-endian audio.

              Non-streamable formats:

              - `aac`: AAC audio codec.
              - `wav`: 16-bit PCM audio in WAV container.

          language: The language of the source audio. Two letter ISO 639-1 code.

          sample_rate: The desired output sample rate in Hz. Defaults to `24000` for all formats except
              `mulaw` which defaults to `8000`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "audio": audio,
                "voice": voice,
                "format": format,
                "language": language,
                "sample_rate": sample_rate,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["audio"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/ai/speech/convert",
            body=maybe_transform(body, speech_convert_params.SpeechConvertParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def generate(
        self,
        *,
        text: str,
        voice: str,
        debug: bool | Omit = omit,
        format: Literal["aac", "mp3", "ulaw", "wav", "webm", "pcm_s16le", "pcm_f32le"] | Omit = omit,
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
        | Omit = omit,
        model: Literal["blizzard"] | Omit = omit,
        sample_rate: Literal[8000, 16000, 24000] | Omit = omit,
        seed: int | Omit = omit,
        temperature: float | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Generates speech from text and streams the audio as binary data chunks in
        real-time as they are generated.

        This is the recommended endpoint for most text-to-speech use cases. You can
        either stream the chunks for low-latency playback or collect all chunks to get
        the complete audio file.

        Args:
          text: The text to synthesize; max 5000 characters per request (including spaces).

          voice: The voice id of the voice to use; voice ids can be retrieved by calls to
              `List voices` or `Voice info`.

          debug: When set to true, the generated speech will also be saved to your
              [clip library](https://app.lmnt.com/clips) in the LMNT playground.

          format: The desired output format of the audio. If you are using a streaming endpoint,
              you'll generate audio faster by selecting a streamable format since chunks are
              encoded and returned as they're generated. For non-streamable formats, the
              entire audio will be synthesized before encoding.

              Streamable formats:

              - `mp3`: 96kbps MP3 audio.
              - `ulaw`: 8-bit G711 µ-law audio with a WAV header.
              - `webm`: WebM format with Opus audio codec.
              - `pcm_s16le`: PCM signed 16-bit little-endian audio.
              - `pcm_f32le`: PCM 32-bit floating-point little-endian audio.

              Non-streamable formats:

              - `aac`: AAC audio codec.
              - `wav`: 16-bit PCM audio in WAV container.

          language: The desired language. Two letter ISO 639-1 code. Defaults to auto language
              detection, but specifying the language is recommended for faster generation.

          model: The model to use for synthesis. Learn more about models
              [here](https://docs.lmnt.com/guides/models).

          sample_rate: The desired output sample rate in Hz. Defaults to `24000` for all formats except
              `mulaw` which defaults to `8000`.

          seed: Seed used to specify a different take; defaults to random

          temperature: Influences how expressive and emotionally varied the speech becomes. Lower
              values (like 0.3) create more neutral, consistent speaking styles. Higher values
              (like 1.0) allow for more dynamic emotional range and speaking styles.

          top_p: Controls the stability of the generated speech. A lower value (like 0.3)
              produces more consistent, reliable speech. A higher value (like 0.9) gives more
              flexibility in how words are spoken, but might occasionally produce unusual
              intonations or speech patterns.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._post(
            "/v1/ai/speech/bytes",
            body=maybe_transform(
                {
                    "text": text,
                    "voice": voice,
                    "debug": debug,
                    "format": format,
                    "language": language,
                    "model": model,
                    "sample_rate": sample_rate,
                    "seed": seed,
                    "temperature": temperature,
                    "top_p": top_p,
                },
                speech_generate_params.SpeechGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def generate_detailed(
        self,
        *,
        text: str,
        voice: str,
        debug: bool | Omit = omit,
        format: Literal["aac", "mp3", "ulaw", "wav", "webm", "pcm_s16le", "pcm_f32le"] | Omit = omit,
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
        | Omit = omit,
        model: Literal["blizzard"] | Omit = omit,
        return_durations: bool | Omit = omit,
        sample_rate: Literal[8000, 16000, 24000] | Omit = omit,
        seed: int | Omit = omit,
        temperature: float | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpeechGenerateDetailedResponse:
        """
        Generates speech from text and returns a JSON object that contains a
        **base64-encoded audio string** and optionally word-level durations
        (timestamps). This endpoint waits for the entire synthesis before responding, so
        it is not ideal for latency-sensitive applications.

        Args:
          text: The text to synthesize; max 5000 characters per request (including spaces).

          voice: The voice id of the voice to use; voice ids can be retrieved by calls to
              `List voices` or `Voice info`.

          debug: When set to true, the generated speech will also be saved to your
              [clip library](https://app.lmnt.com/clips) in the LMNT playground.

          format: The desired output format of the audio. If you are using a streaming endpoint,
              you'll generate audio faster by selecting a streamable format since chunks are
              encoded and returned as they're generated. For non-streamable formats, the
              entire audio will be synthesized before encoding.

              Streamable formats:

              - `mp3`: 96kbps MP3 audio.
              - `ulaw`: 8-bit G711 µ-law audio with a WAV header.
              - `webm`: WebM format with Opus audio codec.
              - `pcm_s16le`: PCM signed 16-bit little-endian audio.
              - `pcm_f32le`: PCM 32-bit floating-point little-endian audio.

              Non-streamable formats:

              - `aac`: AAC audio codec.
              - `wav`: 16-bit PCM audio in WAV container.

          language: The desired language. Two letter ISO 639-1 code. Defaults to auto language
              detection, but specifying the language is recommended for faster generation.

          model: The model to use for synthesis. Learn more about models
              [here](https://docs.lmnt.com/guides/models).

          return_durations: If set as `true`, response will contain a durations object.

          sample_rate: The desired output sample rate in Hz. Defaults to `24000` for all formats except
              `mulaw` which defaults to `8000`.

          seed: Seed used to specify a different take; defaults to random

          temperature: Influences how expressive and emotionally varied the speech becomes. Lower
              values (like 0.3) create more neutral, consistent speaking styles. Higher values
              (like 1.0) allow for more dynamic emotional range and speaking styles.

          top_p: Controls the stability of the generated speech. A lower value (like 0.3)
              produces more consistent, reliable speech. A higher value (like 0.9) gives more
              flexibility in how words are spoken, but might occasionally produce unusual
              intonations or speech patterns.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/ai/speech",
            body=maybe_transform(
                {
                    "text": text,
                    "voice": voice,
                    "debug": debug,
                    "format": format,
                    "language": language,
                    "model": model,
                    "return_durations": return_durations,
                    "sample_rate": sample_rate,
                    "seed": seed,
                    "temperature": temperature,
                    "top_p": top_p,
                },
                speech_generate_detailed_params.SpeechGenerateDetailedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpeechGenerateDetailedResponse,
        )


class AsyncSpeechResource(AsyncAPIResource):
    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        return AsyncSessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSpeechResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lmnt-com/lmnt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpeechResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpeechResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lmnt-com/lmnt-python#with_streaming_response
        """
        return AsyncSpeechResourceWithStreamingResponse(self)

    async def convert(
        self,
        *,
        audio: FileTypes,
        voice: str,
        format: Literal["aac", "mp3", "ulaw", "wav", "webm", "pcm_s16le", "pcm_f32le"] | Omit = omit,
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
        | Omit = omit,
        sample_rate: Literal[8000, 16000, 24000] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Converts speech from one voice to another.

        Args:
          audio: The audio file to be converted into a new voice. Specify source language using
              the `language` parameter. Acceptable formats: `wav`, `mp3`. Max file size: 1 MB.

          voice: The voice id to convert the speech into. Voice ids can be retrieved by calls to
              `List voices` or `Voice info`.

          format: The desired output format of the audio. If you are using a streaming endpoint,
              you'll generate audio faster by selecting a streamable format since chunks are
              encoded and returned as they're generated. For non-streamable formats, the
              entire audio will be synthesized before encoding.

              Streamable formats:

              - `mp3`: 96kbps MP3 audio.
              - `ulaw`: 8-bit G711 µ-law audio with a WAV header.
              - `webm`: WebM format with Opus audio codec.
              - `pcm_s16le`: PCM signed 16-bit little-endian audio.
              - `pcm_f32le`: PCM 32-bit floating-point little-endian audio.

              Non-streamable formats:

              - `aac`: AAC audio codec.
              - `wav`: 16-bit PCM audio in WAV container.

          language: The language of the source audio. Two letter ISO 639-1 code.

          sample_rate: The desired output sample rate in Hz. Defaults to `24000` for all formats except
              `mulaw` which defaults to `8000`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "audio": audio,
                "voice": voice,
                "format": format,
                "language": language,
                "sample_rate": sample_rate,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["audio"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/ai/speech/convert",
            body=await async_maybe_transform(body, speech_convert_params.SpeechConvertParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def generate(
        self,
        *,
        text: str,
        voice: str,
        debug: bool | Omit = omit,
        format: Literal["aac", "mp3", "ulaw", "wav", "webm", "pcm_s16le", "pcm_f32le"] | Omit = omit,
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
        | Omit = omit,
        model: Literal["blizzard"] | Omit = omit,
        sample_rate: Literal[8000, 16000, 24000] | Omit = omit,
        seed: int | Omit = omit,
        temperature: float | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Generates speech from text and streams the audio as binary data chunks in
        real-time as they are generated.

        This is the recommended endpoint for most text-to-speech use cases. You can
        either stream the chunks for low-latency playback or collect all chunks to get
        the complete audio file.

        Args:
          text: The text to synthesize; max 5000 characters per request (including spaces).

          voice: The voice id of the voice to use; voice ids can be retrieved by calls to
              `List voices` or `Voice info`.

          debug: When set to true, the generated speech will also be saved to your
              [clip library](https://app.lmnt.com/clips) in the LMNT playground.

          format: The desired output format of the audio. If you are using a streaming endpoint,
              you'll generate audio faster by selecting a streamable format since chunks are
              encoded and returned as they're generated. For non-streamable formats, the
              entire audio will be synthesized before encoding.

              Streamable formats:

              - `mp3`: 96kbps MP3 audio.
              - `ulaw`: 8-bit G711 µ-law audio with a WAV header.
              - `webm`: WebM format with Opus audio codec.
              - `pcm_s16le`: PCM signed 16-bit little-endian audio.
              - `pcm_f32le`: PCM 32-bit floating-point little-endian audio.

              Non-streamable formats:

              - `aac`: AAC audio codec.
              - `wav`: 16-bit PCM audio in WAV container.

          language: The desired language. Two letter ISO 639-1 code. Defaults to auto language
              detection, but specifying the language is recommended for faster generation.

          model: The model to use for synthesis. Learn more about models
              [here](https://docs.lmnt.com/guides/models).

          sample_rate: The desired output sample rate in Hz. Defaults to `24000` for all formats except
              `mulaw` which defaults to `8000`.

          seed: Seed used to specify a different take; defaults to random

          temperature: Influences how expressive and emotionally varied the speech becomes. Lower
              values (like 0.3) create more neutral, consistent speaking styles. Higher values
              (like 1.0) allow for more dynamic emotional range and speaking styles.

          top_p: Controls the stability of the generated speech. A lower value (like 0.3)
              produces more consistent, reliable speech. A higher value (like 0.9) gives more
              flexibility in how words are spoken, but might occasionally produce unusual
              intonations or speech patterns.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._post(
            "/v1/ai/speech/bytes",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "voice": voice,
                    "debug": debug,
                    "format": format,
                    "language": language,
                    "model": model,
                    "sample_rate": sample_rate,
                    "seed": seed,
                    "temperature": temperature,
                    "top_p": top_p,
                },
                speech_generate_params.SpeechGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def generate_detailed(
        self,
        *,
        text: str,
        voice: str,
        debug: bool | Omit = omit,
        format: Literal["aac", "mp3", "ulaw", "wav", "webm", "pcm_s16le", "pcm_f32le"] | Omit = omit,
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
        | Omit = omit,
        model: Literal["blizzard"] | Omit = omit,
        return_durations: bool | Omit = omit,
        sample_rate: Literal[8000, 16000, 24000] | Omit = omit,
        seed: int | Omit = omit,
        temperature: float | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpeechGenerateDetailedResponse:
        """
        Generates speech from text and returns a JSON object that contains a
        **base64-encoded audio string** and optionally word-level durations
        (timestamps). This endpoint waits for the entire synthesis before responding, so
        it is not ideal for latency-sensitive applications.

        Args:
          text: The text to synthesize; max 5000 characters per request (including spaces).

          voice: The voice id of the voice to use; voice ids can be retrieved by calls to
              `List voices` or `Voice info`.

          debug: When set to true, the generated speech will also be saved to your
              [clip library](https://app.lmnt.com/clips) in the LMNT playground.

          format: The desired output format of the audio. If you are using a streaming endpoint,
              you'll generate audio faster by selecting a streamable format since chunks are
              encoded and returned as they're generated. For non-streamable formats, the
              entire audio will be synthesized before encoding.

              Streamable formats:

              - `mp3`: 96kbps MP3 audio.
              - `ulaw`: 8-bit G711 µ-law audio with a WAV header.
              - `webm`: WebM format with Opus audio codec.
              - `pcm_s16le`: PCM signed 16-bit little-endian audio.
              - `pcm_f32le`: PCM 32-bit floating-point little-endian audio.

              Non-streamable formats:

              - `aac`: AAC audio codec.
              - `wav`: 16-bit PCM audio in WAV container.

          language: The desired language. Two letter ISO 639-1 code. Defaults to auto language
              detection, but specifying the language is recommended for faster generation.

          model: The model to use for synthesis. Learn more about models
              [here](https://docs.lmnt.com/guides/models).

          return_durations: If set as `true`, response will contain a durations object.

          sample_rate: The desired output sample rate in Hz. Defaults to `24000` for all formats except
              `mulaw` which defaults to `8000`.

          seed: Seed used to specify a different take; defaults to random

          temperature: Influences how expressive and emotionally varied the speech becomes. Lower
              values (like 0.3) create more neutral, consistent speaking styles. Higher values
              (like 1.0) allow for more dynamic emotional range and speaking styles.

          top_p: Controls the stability of the generated speech. A lower value (like 0.3)
              produces more consistent, reliable speech. A higher value (like 0.9) gives more
              flexibility in how words are spoken, but might occasionally produce unusual
              intonations or speech patterns.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/ai/speech",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "voice": voice,
                    "debug": debug,
                    "format": format,
                    "language": language,
                    "model": model,
                    "return_durations": return_durations,
                    "sample_rate": sample_rate,
                    "seed": seed,
                    "temperature": temperature,
                    "top_p": top_p,
                },
                speech_generate_detailed_params.SpeechGenerateDetailedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpeechGenerateDetailedResponse,
        )


class SpeechResourceWithRawResponse:
    def __init__(self, speech: SpeechResource) -> None:
        self._speech = speech

        self.convert = to_custom_raw_response_wrapper(
            speech.convert,
            BinaryAPIResponse,
        )
        self.generate = to_custom_raw_response_wrapper(
            speech.generate,
            BinaryAPIResponse,
        )
        self.generate_detailed = to_raw_response_wrapper(
            speech.generate_detailed,
        )


class AsyncSpeechResourceWithRawResponse:
    def __init__(self, speech: AsyncSpeechResource) -> None:
        self._speech = speech

        self.convert = async_to_custom_raw_response_wrapper(
            speech.convert,
            AsyncBinaryAPIResponse,
        )
        self.generate = async_to_custom_raw_response_wrapper(
            speech.generate,
            AsyncBinaryAPIResponse,
        )
        self.generate_detailed = async_to_raw_response_wrapper(
            speech.generate_detailed,
        )


class SpeechResourceWithStreamingResponse:
    def __init__(self, speech: SpeechResource) -> None:
        self._speech = speech

        self.convert = to_custom_streamed_response_wrapper(
            speech.convert,
            StreamedBinaryAPIResponse,
        )
        self.generate = to_custom_streamed_response_wrapper(
            speech.generate,
            StreamedBinaryAPIResponse,
        )
        self.generate_detailed = to_streamed_response_wrapper(
            speech.generate_detailed,
        )


class AsyncSpeechResourceWithStreamingResponse:
    def __init__(self, speech: AsyncSpeechResource) -> None:
        self._speech = speech

        self.convert = async_to_custom_streamed_response_wrapper(
            speech.convert,
            AsyncStreamedBinaryAPIResponse,
        )
        self.generate = async_to_custom_streamed_response_wrapper(
            speech.generate,
            AsyncStreamedBinaryAPIResponse,
        )
        self.generate_detailed = async_to_streamed_response_wrapper(
            speech.generate_detailed,
        )
