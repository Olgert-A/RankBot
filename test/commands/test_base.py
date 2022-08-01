import pytest
from commands.base import CmdExecutor


@pytest.mark.asyncio
async def test_executor():
    class Message:
        def __init__(self, content):
            self.content = content

    class SomeExecutor(CmdExecutor):
        def __init__(self):
            super().__init__()

            self._commands = {
                '/some': self.some,
                '/wparam': self.wparam
            }

        async def some(self, param):
            return 'Some executed'

        async def wparam(self, param):
            return 'With param'

    m1 = Message('/some')
    m2 = Message('/wparam 12 34')
    m3 = Message('some')
    e = SomeExecutor()
    assert await e.execute(m1) == 'Some executed'
    assert await e.execute(m2) == 'With param'
    assert await e.execute(m3) == ''

