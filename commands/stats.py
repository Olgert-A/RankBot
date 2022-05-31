import aiohttp
import logging
from commands.base import CmdExecutor
from stats.checker import StatsChecker


class StatsExecutor(CmdExecutor):
    def __init__(self):
        super().__init__()
        self._commands = {
            '/rank2': self.rank,
            '/match': self.match
        }

    async def rank(self, param):
        logging.debug(f"StatsExecutor.rank: CALLED")
        async with aiohttp.ClientSession() as s:
            steam_id = param[0]
            return await StatsChecker.rank(s, steam_id)

    async def match(self, param):
        logging.debug(f"StatsExecutor.match: CALLED")
        async with aiohttp.ClientSession() as s:
            steam_id = param[0]
            return await StatsChecker.match(s, steam_id)
