import aiohttp
import logging
from commands.base import CmdExecutor
from stats.checker import StatsChecker


class StatsExecutor(CmdExecutor):
    def __init__(self):
        super().__init__()
        self._commands = {
            '/rank': self.rank,
            '/rank2': self.rank
        }

    async def rank(self, params):
        logging.debug(f"StatsExecutor handled '/rank' cmd with parameters: {params}")
        async with aiohttp.ClientSession() as s:
            steam_id = params[0]
            return await StatsChecker.rank(s, steam_id)
