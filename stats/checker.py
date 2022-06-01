import logging

import aiohttp
import asyncio
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

    @staticmethod
    async def match(session: aiohttp.ClientSession, steam_id: str) -> str:
        logging.debug(f"StatsChecker.match: CALLED     steam_id:{steam_id}")
        status, resp = await Api.match(session, steam_id)
        if status != 200:
            logging.warning(f"StatsChecker.match: WARNING     match request return status:{status}")
        try:
            data = json.loads(resp)
            time = format_time(data['last_match']['opened'])
            players_data = sorted(data['last_match']['players'], key=lambda item: (item['team'], item['color']))
            # get ranks of all players
            tasks = [StatsChecker.rank(session, player['steam_id'], player['profile_id']) for player in players_data]
            ranks = await asyncio.gather(*[asyncio.create_task(t) for t in tasks])
            match = [format_match_player(data, rank) for data, rank in zip(players_data, ranks)]
            # build result with timestamp and players rank info
            result = time + '\n'.join(match)
            logging.info(f"StatsChecker.match: SUCCESS     result: {result}")
            return result
        except ValueError:
            logging.exception(f"StatsChecker.match: conversion raise exception")
        return ""
