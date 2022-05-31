import aiohttp
import pytest
from stats.checker import StatsChecker


@pytest.mark.asyncio
async def test_match_checker():
    async with aiohttp.ClientSession() as s:
        result = await StatsChecker.match(s, "76561199231052871") # BEATLEMAN 76561199111768488 | IGRIS 76561199231052871
