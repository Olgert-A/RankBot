import enum
import json
import logging


def calc_winrate(wins: int, losses: int) -> int:
    """calculate winrate using number of wins and number of losses"""
    if (wins + losses) != 0:
        return round(100 * wins / (wins + losses))
    else:
        return 0


def convert_rank(leaderboard: str, status: int, data: str) -> str:
    """parse rank query results into string"""
    logging.debug(f'convert_rank: CALLED     leaderboard: {leaderboard} status: {status} data:{data}')
    if status == 200:
        data = data[1:-1]
        try:
            data = json.loads(data)
            logging.debug(f'convert_rank: unpacked data to json: {data}')
            winrate = calc_winrate(data['num_wins'], data['num_losses'])
            result = f"{leaderboard}:{data['rating']} {winrate}% {data['streak']}"
            logging.debug(f'convert_rank: SUCCESS     result: {result}')
            return result

        except ValueError:
            logging.exception('convert_rank: conversion raise exception')
            return '----'
    else:
        return '----'


class LeaderboardID(enum.Enum):
    S = 3  # SOLO
    TG = 4  # TeamGames
    UNRANKED = 0
