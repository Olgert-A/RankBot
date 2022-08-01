from commands.base import CmdExecutor


class StatsExecutor(CmdExecutor):
    def __init__(self):
        super().__init__()
        self._commands = {
            '/rank': self.rank
        }

    async def rank(self, params):
        return 'rank'
