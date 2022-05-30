import aiohttp
import pytest
from stats.parser import StatsParser


@pytest.mark.asyncio
async def test_rating():
    async with aiohttp.ClientSession() as s:
        result = await StatsParser.rank(s, "76561199111768488", "")
