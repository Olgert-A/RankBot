import aiohttp
import pytest
from stats.api import StatsApi


@pytest.mark.asyncio
async def test_rating():
    leaderboard = 3

    async with aiohttp.ClientSession() as s:
        status, data = await StatsApi.rating(s, "76561198379389049", "", leaderboard)
        assert status

        status, data = await StatsApi.rating(s, "", "3515553", leaderboard)
        assert status

        status, data = await StatsApi.rating(s, "", "", -1)
        assert status

        status, data = await StatsApi.rating(s, "za", "", leaderboard)
        assert status

        status, data = await StatsApi.rating(s, "", "fds", leaderboard)
        assert status