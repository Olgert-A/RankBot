import aiohttp
import logging


async def get_response(session: aiohttp.ClientSession, url: str, params: dict) -> tuple:
    logging.debug(f"get_response called with {url} and {params}")

    async with session.get(url, params=params) as response:
        status = response.status
        text = await response.text()
        logging.debug(f"get_response exit with status:{status} and data:{text}")
        return status, text


class StatsApi:
    @staticmethod
    async def rating(session: aiohttp.ClientSession, steam_id: str, profile_id: int, leaderboard_id: int):
        url = "https://aoe2.net/api/player/ratinghistory"
        params = {
            'game': 'aoe2de',
            'leaderboard_id': f'{leaderboard_id}',
            'start': '0',
            'count': '1'
        }

        logging.debug(f"StatsApi 'rating' method called with url:{url} and params "
                      f"steam:{steam_id} profile:{profile_id} leaderboard:{leaderboard_id}")

        if steam_id and not steam_id.isspace():
            params['steam_id'] = steam_id
        if profile_id:
            params['profile_id'] = profile_id

        return await get_response(session, url, params)