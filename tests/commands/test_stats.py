import pytest
from tests.commands.message import Message
from commands.stats import StatsExecutor


@pytest.mark.asyncio
async def test_stats():
    empty1 = Message('')
    empty2 = Message(' ')
    rank = Message('/rank')
    rank_param = Message('/rank 12 34')
    trash = Message('trash  data 1 ')

    stats = StatsExecutor()

    assert await stats.execute(empty1) == ''
    assert await stats.execute(empty2) == ''
    assert await stats.execute(rank) != ''
    assert await stats.execute(rank_param) != ''
    assert await stats.execute(trash) == ''
