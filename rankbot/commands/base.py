class CmdExecutor:
    """Base chat commands container, which implement execute method for it"""

    def __init__(self):
        self._commands = {}
        self.msg = None

    async def execute(self, message) -> str:
        """reads command from message and executes helper method for it"""
        self.msg = message
        split = message.content.split()

        try:
            cmd = split[0]
            params = split[1:]
        except IndexError:
            return ''

        if cmd in self._commands:
            return await self._commands[cmd](params)
        return ''


class CmdParser:
    """Container with executors for different command groups"""

    def __init__(self):
        self._executors = []

    def add(self, cmd_executor) -> None:
        self._executors.append(cmd_executor)

    def delete(self, cmd_executor) -> None:
        if cmd_executor in self._executors:
            self._executors.remove(cmd_executor)

    async def parse(self, message) -> str:
        """executes all parsers to process cmd"""
        for e in self._executors:
            result = await e.execute(message)
            if result:
                return result
        return ''
