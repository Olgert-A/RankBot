import aiohttp
import json
import pytest
from stats.api import get_response


@pytest.mark.asyncio
async def test_get_response():
    url = "https://fakerapi.it/api/v1/custom"
    params = {
        '_quantity': '1',
        'field': 'boolean'
    }

    async with aiohttp.ClientSession() as s:
        status, data = await get_response(s, url, params)
        data = json.loads(data)
        assert status
        assert data["total"] == 1
