# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..types import voice_list_params, voice_create_params, voice_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.voice import Voice
from .._base_client import make_request_options
from ..types.voice_list_response import VoiceListResponse
from ..types.voice_delete_response import VoiceDeleteResponse
from ..types.voice_update_response import VoiceUpdateResponse

__all__ = ["VoicesResource", "AsyncVoicesResource"]


class VoicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lmnt-com/lmnt-python#accessing-raw-response-data-eg-headers
        """
        return VoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lmnt-com/lmnt-python#with_streaming_response
        """
        return VoicesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        enhance: bool,
        files: SequenceNotStr[FileTypes],
        name: str,
        description: str | Omit = omit,
        gender: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Voice:
        """
        Submits a request to create a voice with a supplied voice configuration and a
        batch of input audio data.

        Args:
          enhance: For unclean audio with background noise, applies processing to attempt to
              improve quality. Default is `false` as this can also degrade quality in some
              circumstances.

          files: One or more input audio files to train the voice in the form of binary `wav`,
              `mp3`, `mp4`, `m4a`, or `webm` attachments.

              - Max attached files: 20.
              - Max total file size: 250 MB.

          name: The display name for this voice

          description: A text description of this voice.

          gender: A tag describing the gender of this voice. Has no effect on voice creation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "enhance": enhance,
                "files": files,
                "name": name,
                "description": description,
                "gender": gender,
            }
        )
        extracted_files = extract_files(cast(Mapping[str, object], body), paths=[["files", "<array>"]])
        # Remove the files from the body since they are now in extracted_files
        body.pop("files", None)
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/ai/voice",
            body=maybe_transform(body, voice_create_params.VoiceCreateParams),
            files=extracted_files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Voice,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Voice:
        """
        Returns details of a specific voice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/ai/voice/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Voice,
        )

    def update(
        self,
        id: str,
        *,
        description: str | Omit = omit,
        gender: str | Omit = omit,
        name: str | Omit = omit,
        starred: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceUpdateResponse:
        """Updates metadata for a specific voice.

        Only provided fields will be changed.

        Args:
          description: A description of this voice.

          gender: A tag describing the gender of this voice, e.g. `male`, `female`, `nonbinary`.

          name: The display name for this voice.

          starred: If `true`, adds this voice to your starred list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/v1/ai/voice/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "gender": gender,
                    "name": name,
                    "starred": starred,
                },
                voice_update_params.VoiceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceUpdateResponse,
        )

    def list(
        self,
        *,
        owner: str | Omit = omit,
        starred: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceListResponse:
        """
        Returns a list of voices available to you.

        Args:
          owner: Which owner's voices to return. Choose from `system`, `me`, or `all`.

          starred: If true, only returns voices that you have starred.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/ai/voice/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "owner": owner,
                        "starred": starred,
                    },
                    voice_list_params.VoiceListParams,
                ),
            ),
            cast_to=VoiceListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceDeleteResponse:
        """Deletes a voice and cancels any pending operations on it.

        Cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/v1/ai/voice/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceDeleteResponse,
        )


class AsyncVoicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lmnt-com/lmnt-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lmnt-com/lmnt-python#with_streaming_response
        """
        return AsyncVoicesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        enhance: bool,
        files: SequenceNotStr[FileTypes],
        name: str,
        description: str | Omit = omit,
        gender: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Voice:
        """
        Submits a request to create a voice with a supplied voice configuration and a
        batch of input audio data.

        Args:
          enhance: For unclean audio with background noise, applies processing to attempt to
              improve quality. Default is `false` as this can also degrade quality in some
              circumstances.

          files: One or more input audio files to train the voice in the form of binary `wav`,
              `mp3`, `mp4`, `m4a`, or `webm` attachments.

              - Max attached files: 20.
              - Max total file size: 250 MB.

          name: The display name for this voice

          description: A text description of this voice.

          gender: A tag describing the gender of this voice. Has no effect on voice creation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "enhance": enhance,
                "files": files,
                "name": name,
                "description": description,
                "gender": gender,
            }
        )
        extracted_files = extract_files(cast(Mapping[str, object], body), paths=[["files", "<array>"]])
        # Remove the files from the body since they are now in extracted_files
        body.pop("files", None)
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/ai/voice",
            body=await async_maybe_transform(body, voice_create_params.VoiceCreateParams),
            files=extracted_files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Voice,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Voice:
        """
        Returns details of a specific voice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/ai/voice/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Voice,
        )

    async def update(
        self,
        id: str,
        *,
        description: str | Omit = omit,
        gender: str | Omit = omit,
        name: str | Omit = omit,
        starred: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceUpdateResponse:
        """Updates metadata for a specific voice.

        Only provided fields will be changed.

        Args:
          description: A description of this voice.

          gender: A tag describing the gender of this voice, e.g. `male`, `female`, `nonbinary`.

          name: The display name for this voice.

          starred: If `true`, adds this voice to your starred list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/v1/ai/voice/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "gender": gender,
                    "name": name,
                    "starred": starred,
                },
                voice_update_params.VoiceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceUpdateResponse,
        )

    async def list(
        self,
        *,
        owner: str | Omit = omit,
        starred: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceListResponse:
        """
        Returns a list of voices available to you.

        Args:
          owner: Which owner's voices to return. Choose from `system`, `me`, or `all`.

          starred: If true, only returns voices that you have starred.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/ai/voice/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "owner": owner,
                        "starred": starred,
                    },
                    voice_list_params.VoiceListParams,
                ),
            ),
            cast_to=VoiceListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceDeleteResponse:
        """Deletes a voice and cancels any pending operations on it.

        Cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/v1/ai/voice/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceDeleteResponse,
        )


class VoicesResourceWithRawResponse:
    def __init__(self, voices: VoicesResource) -> None:
        self._voices = voices

        self.create = to_raw_response_wrapper(
            voices.create,
        )
        self.retrieve = to_raw_response_wrapper(
            voices.retrieve,
        )
        self.update = to_raw_response_wrapper(
            voices.update,
        )
        self.list = to_raw_response_wrapper(
            voices.list,
        )
        self.delete = to_raw_response_wrapper(
            voices.delete,
        )


class AsyncVoicesResourceWithRawResponse:
    def __init__(self, voices: AsyncVoicesResource) -> None:
        self._voices = voices

        self.create = async_to_raw_response_wrapper(
            voices.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            voices.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            voices.update,
        )
        self.list = async_to_raw_response_wrapper(
            voices.list,
        )
        self.delete = async_to_raw_response_wrapper(
            voices.delete,
        )


class VoicesResourceWithStreamingResponse:
    def __init__(self, voices: VoicesResource) -> None:
        self._voices = voices

        self.create = to_streamed_response_wrapper(
            voices.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            voices.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            voices.update,
        )
        self.list = to_streamed_response_wrapper(
            voices.list,
        )
        self.delete = to_streamed_response_wrapper(
            voices.delete,
        )


class AsyncVoicesResourceWithStreamingResponse:
    def __init__(self, voices: AsyncVoicesResource) -> None:
        self._voices = voices

        self.create = async_to_streamed_response_wrapper(
            voices.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            voices.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            voices.update,
        )
        self.list = async_to_streamed_response_wrapper(
            voices.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            voices.delete,
        )
