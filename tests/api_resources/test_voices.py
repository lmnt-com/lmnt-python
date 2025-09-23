# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lmnt import Lmnt, AsyncLmnt
from lmnt.types import (
    Voice,
    VoiceListResponse,
    VoiceDeleteResponse,
    VoiceUpdateResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVoices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism bug detailed here: https://github.com/stoplightio/prism/pull/2654")
    @parametrize
    def test_method_create(self, client: Lmnt) -> None:
        voice = client.voices.create(
            enhance=False,
            files=[b"raw file contents"],
            name="new-voice",
        )
        assert_matches_type(Voice, voice, path=["response"])

    @pytest.mark.skip(reason="Prism bug detailed here: https://github.com/stoplightio/prism/pull/2654")
    @parametrize
    def test_method_create_with_all_params(self, client: Lmnt) -> None:
        voice = client.voices.create(
            enhance=False,
            files=[b"raw file contents"],
            name="new-voice",
            description="description",
            gender="gender",
        )
        assert_matches_type(Voice, voice, path=["response"])

    @pytest.mark.skip(reason="Prism bug detailed here: https://github.com/stoplightio/prism/pull/2654")
    @parametrize
    def test_raw_response_create(self, client: Lmnt) -> None:
        response = client.voices.with_raw_response.create(
            enhance=False,
            files=[b"raw file contents"],
            name="new-voice",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(Voice, voice, path=["response"])

    @pytest.mark.skip(reason="Prism bug detailed here: https://github.com/stoplightio/prism/pull/2654")
    @parametrize
    def test_streaming_response_create(self, client: Lmnt) -> None:
        with client.voices.with_streaming_response.create(
            enhance=False,
            files=[b"raw file contents"],
            name="new-voice",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(Voice, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Lmnt) -> None:
        voice = client.voices.retrieve(
            "123",
        )
        assert_matches_type(Voice, voice, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lmnt) -> None:
        response = client.voices.with_raw_response.retrieve(
            "123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(Voice, voice, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lmnt) -> None:
        with client.voices.with_streaming_response.retrieve(
            "123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(Voice, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lmnt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.voices.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Lmnt) -> None:
        voice = client.voices.update(
            id="123",
        )
        assert_matches_type(VoiceUpdateResponse, voice, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Lmnt) -> None:
        voice = client.voices.update(
            id="123",
            description="description",
            gender="gender",
            name="name",
            starred=True,
        )
        assert_matches_type(VoiceUpdateResponse, voice, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Lmnt) -> None:
        response = client.voices.with_raw_response.update(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(VoiceUpdateResponse, voice, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Lmnt) -> None:
        with client.voices.with_streaming_response.update(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(VoiceUpdateResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Lmnt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.voices.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Lmnt) -> None:
        voice = client.voices.list()
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lmnt) -> None:
        voice = client.voices.list(
            owner="owner",
            starred="starred",
        )
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lmnt) -> None:
        response = client.voices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lmnt) -> None:
        with client.voices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(VoiceListResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Lmnt) -> None:
        voice = client.voices.delete(
            "123",
        )
        assert_matches_type(VoiceDeleteResponse, voice, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Lmnt) -> None:
        response = client.voices.with_raw_response.delete(
            "123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(VoiceDeleteResponse, voice, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Lmnt) -> None:
        with client.voices.with_streaming_response.delete(
            "123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(VoiceDeleteResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Lmnt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.voices.with_raw_response.delete(
                "",
            )


class TestAsyncVoices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism bug detailed here: https://github.com/stoplightio/prism/pull/2654")
    @parametrize
    async def test_method_create(self, async_client: AsyncLmnt) -> None:
        voice = await async_client.voices.create(
            enhance=False,
            files=[b"raw file contents"],
            name="new-voice",
        )
        assert_matches_type(Voice, voice, path=["response"])

    @pytest.mark.skip(reason="Prism bug detailed here: https://github.com/stoplightio/prism/pull/2654")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLmnt) -> None:
        voice = await async_client.voices.create(
            enhance=False,
            files=[b"raw file contents"],
            name="new-voice",
            description="description",
            gender="gender",
        )
        assert_matches_type(Voice, voice, path=["response"])

    @pytest.mark.skip(reason="Prism bug detailed here: https://github.com/stoplightio/prism/pull/2654")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLmnt) -> None:
        response = await async_client.voices.with_raw_response.create(
            enhance=False,
            files=[b"raw file contents"],
            name="new-voice",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(Voice, voice, path=["response"])

    @pytest.mark.skip(reason="Prism bug detailed here: https://github.com/stoplightio/prism/pull/2654")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLmnt) -> None:
        async with async_client.voices.with_streaming_response.create(
            enhance=False,
            files=[b"raw file contents"],
            name="new-voice",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(Voice, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLmnt) -> None:
        voice = await async_client.voices.retrieve(
            "123",
        )
        assert_matches_type(Voice, voice, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLmnt) -> None:
        response = await async_client.voices.with_raw_response.retrieve(
            "123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(Voice, voice, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLmnt) -> None:
        async with async_client.voices.with_streaming_response.retrieve(
            "123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(Voice, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLmnt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.voices.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLmnt) -> None:
        voice = await async_client.voices.update(
            id="123",
        )
        assert_matches_type(VoiceUpdateResponse, voice, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLmnt) -> None:
        voice = await async_client.voices.update(
            id="123",
            description="description",
            gender="gender",
            name="name",
            starred=True,
        )
        assert_matches_type(VoiceUpdateResponse, voice, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLmnt) -> None:
        response = await async_client.voices.with_raw_response.update(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(VoiceUpdateResponse, voice, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLmnt) -> None:
        async with async_client.voices.with_streaming_response.update(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(VoiceUpdateResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLmnt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.voices.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLmnt) -> None:
        voice = await async_client.voices.list()
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLmnt) -> None:
        voice = await async_client.voices.list(
            owner="owner",
            starred="starred",
        )
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLmnt) -> None:
        response = await async_client.voices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLmnt) -> None:
        async with async_client.voices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(VoiceListResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLmnt) -> None:
        voice = await async_client.voices.delete(
            "123",
        )
        assert_matches_type(VoiceDeleteResponse, voice, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLmnt) -> None:
        response = await async_client.voices.with_raw_response.delete(
            "123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(VoiceDeleteResponse, voice, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLmnt) -> None:
        async with async_client.voices.with_streaming_response.delete(
            "123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(VoiceDeleteResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLmnt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.voices.with_raw_response.delete(
                "",
            )
