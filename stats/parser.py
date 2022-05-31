import aiohttp
import asyncio
from stats.api import StatsApi as Api
from stats.misc import *


class StatsParser:
    @staticmethod
    async def rank(session: aiohttp.ClientSession, steam_id: str, profile_id: str) -> str:
        leaderboards = [lb for lb in LeaderboardID if lb != LeaderboardID.UNRANKED]
        tasks = [Api.rating(session, steam_id, profile_id, lb.value) for lb in leaderboards]
        ranks_raw = await asyncio.gather(*[asyncio.create_task(t) for t in tasks])
        ranks = [convert_rank(lb.name, status, data) for lb, (status, data) in zip(leaderboards, ranks_raw)]
        logging.info(f"StatsParser.rank: SUCCESS     result: {ranks}")
        return ' | '.join(ranks)

    @staticmethod
    async def match(session: aiohttp.ClientSession, steam_id: str) -> str:
        pass
