import logging


class CmdExecutor:
    """Base chat commands container, which implement execute method for it"""

    def __init__(self):
        self._commands = {}
        self.msg = None

    async def execute(self, message) -> str:
        """reads command from message and executes helper method for it"""
        logging.debug("CmdExecutor 'execute' method called with message: %s", message.content)
        self.msg = message
        split = message.content.split()

        try:
            cmd = split[0]
            params = split[1:]
        except IndexError:
            logging.debug("CmdExecutor 'execute' method raise IndexError exception")
            return ''

        logging.debug(f"CmdExecutor split message to cmd '{cmd}' and params '{params}'")
        if cmd in self._commands:
            logging.info(f"CmdExecutor find command '{cmd}' and call handled method with params '{params}'")
            return await self._commands[cmd](params)
        return ''


class CmdParser:
    """Container with executors for different command groups"""

    def __init__(self):
        self._executors = []

    def add(self, cmd_executor) -> None:
        logging.debug("CmdParser 'add' method called with param: %s", cmd_executor)

        if cmd_executor not in self._executors:
            self._executors.append(cmd_executor)
            logging.info("New executor '%s' added in parser. Parser now contain: %s", cmd_executor, self._executors)

    def delete(self, cmd_executor) -> None:
        logging.debug("CmdParser 'delete' method called with param: %s", cmd_executor)

        if cmd_executor in self._executors:
            self._executors.remove(cmd_executor)
            logging.info("Executor '%s' deleted from parser. Parser now contain: %s", cmd_executor, self._executors)

    async def parse(self, message) -> str:
        """Executes all parsers to process cmd

        :return: some data string if success else empty string
        """
        logging.debug("CmdParser 'parse' method called with message: %s", message)

        for e in self._executors:
            result = await e.execute(message)
            if result:
                logging.info("Parser 'parse' method successful with result: %s", result)
                return result
        return ''
