import pytest
from commands.base import *


@pytest.mark.asyncio
async def test_executor():
    # define different messages
    trash = Message('trash data 1 ')
    empty1 = Message('')
    empty2 = Message(' ')
    some_msg = Message('/some')
    some_param_msg = Message('/sparam 12 34')
    another_msg = Message('/another')
    another_param_msg = Message('/aparam 56 test')

    some = SomeExecutor()
    another = AnotherExecutor()
    parser = CmdParser()
    parser.add(some)
    parser.add(some)
    parser.add(another)
    parser.delete(another)
    parser.add(another)

    assert await some.execute(some_msg) == 'Some'
    assert await some.execute(some_param_msg) == 'Some with param'
    assert await some.execute(empty1) == ''
    assert await some.execute(empty2) == ''
    assert await some.execute(trash) == ''
    assert await some.execute(another_msg) == ''
    assert await some.execute(another_param_msg) == ''

    assert await another.execute(some_msg) == ''
    assert await another.execute(some_param_msg) == ''
    assert await another.execute(empty1) == ''
    assert await another.execute(empty2) == ''
    assert await another.execute(trash) == ''
    assert await another.execute(another_msg) == 'Another'
    assert await another.execute(another_param_msg) == 'Another with param'

    assert await parser.parse(some_msg) == 'Some'
    assert await parser.parse(some_param_msg) == 'Some with param'
    assert await parser.parse(empty1) == ''
    assert await parser.parse(empty2) == ''
    assert await parser.parse(trash) == ''
    assert await parser.parse(another_msg) == 'Another'
    assert await parser.parse(another_param_msg) == 'Another with param'


class Message:
    """example of discord message object"""
    def __init__(self, content):
        self.content = content


class SomeExecutor(CmdExecutor):
    """
    Some implementation of CmdExecutor which contains two commands with handlers
    one without params and one with
    """

    def __init__(self):
        super().__init__()

        self._commands = {
            '/some': self.some,
            '/sparam': self.sparam
        }

    async def some(self, param):
        logging.info("SomeExecutor handled '/some' cmd")
        return "Some"

    async def sparam(self, param):
        logging.info("SomeExecutor handled '/sparam' cmd with parameters: %s", param)
        return "Some with param"


class AnotherExecutor(CmdExecutor):
    """
    Another implementation of CmdExecutor which contains two commands with handlers
    one without params and one with
    """

    def __init__(self):
        super().__init__()

        self._commands = {
            '/another': self.another,
            '/aparam': self.aparam
        }

    async def another(self, param):
        logging.info("AnotherExecutor handled '/another' cmd")
        return "Another"

    async def aparam(self, param):
        logging.info("AnotherExecutor handled '/aparam' cmd with parameters: %s", param)
        return "Another with param"
