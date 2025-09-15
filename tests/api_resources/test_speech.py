# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from lmnt import Lmnt, AsyncLmnt
from lmnt.types import (
    SpeechGenerateDetailedResponse,
)
from tests.utils import assert_matches_type
from lmnt._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpeech:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_convert(self, client: Lmnt, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/ai/speech/convert").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = client.speech.convert(
            audio=b"raw file contents",
            voice="leah",
        )
        assert speech.is_closed
        assert speech.json() == {"foo": "bar"}
        assert cast(Any, speech.is_closed) is True
        assert isinstance(speech, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_convert_with_all_params(self, client: Lmnt, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/ai/speech/convert").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = client.speech.convert(
            audio=b"raw file contents",
            voice="leah",
            format="aac",
            language="auto",
            sample_rate=8000,
        )
        assert speech.is_closed
        assert speech.json() == {"foo": "bar"}
        assert cast(Any, speech.is_closed) is True
        assert isinstance(speech, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_convert(self, client: Lmnt, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/ai/speech/convert").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        speech = client.speech.with_raw_response.convert(
            audio=b"raw file contents",
            voice="leah",
        )

        assert speech.is_closed is True
        assert speech.http_request.headers.get("X-Stainless-Lang") == "python"
        assert speech.json() == {"foo": "bar"}
        assert isinstance(speech, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_convert(self, client: Lmnt, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/ai/speech/convert").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.speech.with_streaming_response.convert(
            audio=b"raw file contents",
            voice="leah",
        ) as speech:
            assert not speech.is_closed
            assert speech.http_request.headers.get("X-Stainless-Lang") == "python"

            assert speech.json() == {"foo": "bar"}
            assert cast(Any, speech.is_closed) is True
            assert isinstance(speech, StreamedBinaryAPIResponse)

        assert cast(Any, speech.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_generate(self, client: Lmnt, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/ai/speech/bytes").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = client.speech.generate(
            text="hello world.",
            voice="leah",
        )
        assert speech.is_closed
        assert speech.json() == {"foo": "bar"}
        assert cast(Any, speech.is_closed) is True
        assert isinstance(speech, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_generate_with_all_params(self, client: Lmnt, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/ai/speech/bytes").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = client.speech.generate(
            text="hello world.",
            voice="leah",
            debug=True,
            format="aac",
            language="auto",
            model="blizzard",
            sample_rate=8000,
            seed=0,
            temperature=0,
            top_p=0,
        )
        assert speech.is_closed
        assert speech.json() == {"foo": "bar"}
        assert cast(Any, speech.is_closed) is True
        assert isinstance(speech, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_generate(self, client: Lmnt, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/ai/speech/bytes").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        speech = client.speech.with_raw_response.generate(
            text="hello world.",
            voice="leah",
        )

        assert speech.is_closed is True
        assert speech.http_request.headers.get("X-Stainless-Lang") == "python"
        assert speech.json() == {"foo": "bar"}
        assert isinstance(speech, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_generate(self, client: Lmnt, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/ai/speech/bytes").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.speech.with_streaming_response.generate(
            text="hello world.",
            voice="leah",
        ) as speech:
            assert not speech.is_closed
            assert speech.http_request.headers.get("X-Stainless-Lang") == "python"

            assert speech.json() == {"foo": "bar"}
            assert cast(Any, speech.is_closed) is True
            assert isinstance(speech, StreamedBinaryAPIResponse)

        assert cast(Any, speech.is_closed) is True

    @parametrize
    def test_method_generate_detailed(self, client: Lmnt) -> None:
        speech = client.speech.generate_detailed(
            text="hello world.",
            voice="leah",
        )
        assert_matches_type(SpeechGenerateDetailedResponse, speech, path=["response"])

    @parametrize
    def test_method_generate_detailed_with_all_params(self, client: Lmnt) -> None:
        speech = client.speech.generate_detailed(
            text="hello world.",
            voice="leah",
            debug=True,
            format="aac",
            language="auto",
            model="blizzard",
            return_durations=True,
            sample_rate=8000,
            seed=0,
            temperature=0,
            top_p=0,
        )
        assert_matches_type(SpeechGenerateDetailedResponse, speech, path=["response"])

    @parametrize
    def test_raw_response_generate_detailed(self, client: Lmnt) -> None:
        response = client.speech.with_raw_response.generate_detailed(
            text="hello world.",
            voice="leah",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speech = response.parse()
        assert_matches_type(SpeechGenerateDetailedResponse, speech, path=["response"])

    @parametrize
    def test_streaming_response_generate_detailed(self, client: Lmnt) -> None:
        with client.speech.with_streaming_response.generate_detailed(
            text="hello world.",
            voice="leah",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speech = response.parse()
            assert_matches_type(SpeechGenerateDetailedResponse, speech, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSpeech:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_convert(self, async_client: AsyncLmnt, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/ai/speech/convert").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = await async_client.speech.convert(
            audio=b"raw file contents",
            voice="leah",
        )
        assert speech.is_closed
        assert await speech.json() == {"foo": "bar"}
        assert cast(Any, speech.is_closed) is True
        assert isinstance(speech, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_convert_with_all_params(self, async_client: AsyncLmnt, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/ai/speech/convert").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = await async_client.speech.convert(
            audio=b"raw file contents",
            voice="leah",
            format="aac",
            language="auto",
            sample_rate=8000,
        )
        assert speech.is_closed
        assert await speech.json() == {"foo": "bar"}
        assert cast(Any, speech.is_closed) is True
        assert isinstance(speech, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_convert(self, async_client: AsyncLmnt, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/ai/speech/convert").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        speech = await async_client.speech.with_raw_response.convert(
            audio=b"raw file contents",
            voice="leah",
        )

        assert speech.is_closed is True
        assert speech.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await speech.json() == {"foo": "bar"}
        assert isinstance(speech, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_convert(self, async_client: AsyncLmnt, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/ai/speech/convert").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.speech.with_streaming_response.convert(
            audio=b"raw file contents",
            voice="leah",
        ) as speech:
            assert not speech.is_closed
            assert speech.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await speech.json() == {"foo": "bar"}
            assert cast(Any, speech.is_closed) is True
            assert isinstance(speech, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, speech.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_generate(self, async_client: AsyncLmnt, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/ai/speech/bytes").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = await async_client.speech.generate(
            text="hello world.",
            voice="leah",
        )
        assert speech.is_closed
        assert await speech.json() == {"foo": "bar"}
        assert cast(Any, speech.is_closed) is True
        assert isinstance(speech, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_generate_with_all_params(self, async_client: AsyncLmnt, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/ai/speech/bytes").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = await async_client.speech.generate(
            text="hello world.",
            voice="leah",
            debug=True,
            format="aac",
            language="auto",
            model="blizzard",
            sample_rate=8000,
            seed=0,
            temperature=0,
            top_p=0,
        )
        assert speech.is_closed
        assert await speech.json() == {"foo": "bar"}
        assert cast(Any, speech.is_closed) is True
        assert isinstance(speech, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_generate(self, async_client: AsyncLmnt, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/ai/speech/bytes").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        speech = await async_client.speech.with_raw_response.generate(
            text="hello world.",
            voice="leah",
        )

        assert speech.is_closed is True
        assert speech.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await speech.json() == {"foo": "bar"}
        assert isinstance(speech, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_generate(self, async_client: AsyncLmnt, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/ai/speech/bytes").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.speech.with_streaming_response.generate(
            text="hello world.",
            voice="leah",
        ) as speech:
            assert not speech.is_closed
            assert speech.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await speech.json() == {"foo": "bar"}
            assert cast(Any, speech.is_closed) is True
            assert isinstance(speech, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, speech.is_closed) is True

    @parametrize
    async def test_method_generate_detailed(self, async_client: AsyncLmnt) -> None:
        speech = await async_client.speech.generate_detailed(
            text="hello world.",
            voice="leah",
        )
        assert_matches_type(SpeechGenerateDetailedResponse, speech, path=["response"])

    @parametrize
    async def test_method_generate_detailed_with_all_params(self, async_client: AsyncLmnt) -> None:
        speech = await async_client.speech.generate_detailed(
            text="hello world.",
            voice="leah",
            debug=True,
            format="aac",
            language="auto",
            model="blizzard",
            return_durations=True,
            sample_rate=8000,
            seed=0,
            temperature=0,
            top_p=0,
        )
        assert_matches_type(SpeechGenerateDetailedResponse, speech, path=["response"])

    @parametrize
    async def test_raw_response_generate_detailed(self, async_client: AsyncLmnt) -> None:
        response = await async_client.speech.with_raw_response.generate_detailed(
            text="hello world.",
            voice="leah",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speech = await response.parse()
        assert_matches_type(SpeechGenerateDetailedResponse, speech, path=["response"])

    @parametrize
    async def test_streaming_response_generate_detailed(self, async_client: AsyncLmnt) -> None:
        async with async_client.speech.with_streaming_response.generate_detailed(
            text="hello world.",
            voice="leah",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speech = await response.parse()
            assert_matches_type(SpeechGenerateDetailedResponse, speech, path=["response"])

        assert cast(Any, response.is_closed) is True
