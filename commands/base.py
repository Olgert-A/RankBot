import logging


class CmdExecutor:
    """Base chat commands container, which implement execute method for it"""

    def __init__(self):
        self._commands = {}
        self.msg = None

    def __repr__(self):
        return self.__class__.__name__

    async def execute(self, message) -> str:
        """reads command from message and executes helper method for it"""
        logging.debug(f"CmdExecutor.execute: CALLED")
        self.msg = message
        split = message.content.split()

        try:
            cmd = split[0]
            params = split[1:]
        except IndexError:
            logging.debug("CmdExecutor.execute: split raise exception")
            return ''

        logging.debug(f"CmdExecutor.execute: split message to cmd:'{cmd}' and params:'{params}'")
        if cmd in self._commands:
            logging.debug(f"CmdExecutor.execute: SUCCESS     command handle method called")
            return await self._commands[cmd](params)

        logging.debug(f"CmdExecutor.execute: SKIPPED     command not found")
        return ''


class CmdParser:
    """Container with executors for different command groups"""

    def __init__(self):
        self._executors = []

    def add(self, cmd_executor) -> None:
        logging.debug(f"CmdParser.add: CALLED     param:{cmd_executor}")

        if cmd_executor not in self._executors:
            self._executors.append(cmd_executor)
            logging.debug(f"CmdParser.add: SUCCESS     executors in parser:{self._executors}")

    def delete(self, cmd_executor) -> None:
        logging.debug(f"CmdParser.delete: CALLED     param:{cmd_executor}")

        if cmd_executor in self._executors:
            self._executors.remove(cmd_executor)
            logging.debug(f"CmdParser.delete: SUCCESS     executors in parser:{self._executors}")

    async def parse(self, message) -> str:
        """Executes all parsers to process cmd

        :return: some data string if success else empty string
        """
        logging.debug(f"CmdParser.parse: CALLED     message:'{message}'")

        for e in self._executors:
            result = await e.execute(message)
            if result:
                logging.info(f"CmdParser.parse: SUCCESS     result:{result}")
                return result

        logging.info(f"CmdParser.parse: SKIPPED")
        return ''
