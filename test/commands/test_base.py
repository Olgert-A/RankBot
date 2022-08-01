import pytest
from commands.base import CmdParser
from commands.stats import StatsExecutor

# =======some data for next base tests=========


class Message:
    def __init__(self, content):
        self.content = content


empty1 = Message('')
empty2 = Message(' ')
rank = Message('/rank')
rank_param = Message('/rank 12 34')
trash = Message('trash  data 1 ')

# =============================================


@pytest.mark.asyncio
async def test_executor():
    stats = StatsExecutor()

    assert await stats.execute(empty1) == ''
    assert await stats.execute(empty2) == ''
    assert await stats.execute(rank) != ''
    assert await stats.execute(rank_param) != ''
    assert await stats.execute(trash) == ''


@pytest.mark.asyncio
async def test_parser():
    stats1 = StatsExecutor()
    stats2 = StatsExecutor()
    parser = CmdParser()

    parser.add(stats1)
    parser.add(stats2)
    parser.add(stats1)
    parser.delete(stats2)

    assert await parser.parse(empty1) == ''
    assert await parser.parse(empty2) == ''
    assert await parser.parse(rank) != ''
    assert await parser.parse(rank_param) != ''
    assert await parser.parse(trash) == ''
