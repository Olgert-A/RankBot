import aiohttp
import pytest
from stats.checker import StatsChecker


@pytest.mark.asyncio
async def test_rating_checker():
    async with aiohttp.ClientSession() as s:
        result = await StatsChecker.rank(s, "76561199111768488", "")
