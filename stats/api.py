import aiohttp


async def get_response(session: aiohttp.ClientSession, url: str, params: dict) -> tuple:
    async with session.get(url, params=params) as response:
        return response.status, await response.text()


class StatsApi:
    @staticmethod
    async def rating(session, steam_id: str, profile_id: str, leaderboard_id: int):
        url = "https://aoe2.net/api/player/ratinghistory"
        params = {
            'game': 'aoe2de',
            'leaderboard_id': f'{leaderboard_id}',
            'start': '0',
            'count': '1'
        }

        if steam_id and steam_id != '':
            params['steam_id'] = steam_id
        if profile_id and profile_id != '':
            params['profile_id'] = profile_id

        return await get_response(session, url, params)
