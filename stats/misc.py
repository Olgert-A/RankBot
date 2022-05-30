import enum
import json
import logging


def formatted(resp: str) -> str:
    """remove brackets [] in rating response"""
    return resp[1:len(resp) - 1]


def convert_rank(status: int, data: str) -> str:
    if status == 200:
        data = formatted(data)
        try:
            data = json.loads(data)
            wins = int(data['num_wins'])
            loses = data['num_losses']
            winrate = round(100 * wins / (wins + loses))
            return f"{data['rating']} {winrate}% {data['streak']}"

        except ValueError:
            logging.debug('Rank conversion raise exception')
            return '----'
    else:
        return '----'


class LeaderboardID(enum.Enum):
    S = 3  # SOLO
    TG = 4  # TG
    UNRANKED = 0