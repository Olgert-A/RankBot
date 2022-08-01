import aiohttp
import asyncio
import logging
from stats.api import StatsApi as Api
from stats.misc import *


class StatsChecker:
    @staticmethod
    async def rank(session: aiohttp.ClientSession, steam_id: str, profile_id: int = 0) -> str:
        logging.debug(f"StatsChecker.rank: CALLED     steam_id:{steam_id} profile_id:{profile_id}")
        leaderboards = [lb for lb in LeaderboardID if lb != LeaderboardID.UNRANKED]
        tasks = [Api.rating(session, steam_id, profile_id, lb.value) for lb in leaderboards]
        ranks_raw = await asyncio.gather(*[asyncio.create_task(t) for t in tasks])
        ranks = [convert_rank(lb.name, status, data) for lb, (status, data) in zip(leaderboards, ranks_raw)]
        logging.info(f"StatsChecker.rank: SUCCESS     result: {ranks}")
        return ' | '.join(ranks)