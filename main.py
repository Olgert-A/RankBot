import logging
import os
import discord
from commands.base import CmdParser
from commands.stats import StatsExecutor

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")  # get discord token from
discord_client = discord.Client()
logging.basicConfig(level=logging.DEBUG)

stats = StatsExecutor()
parser = CmdParser()
parser.add(stats)


@discord_client.event
async def on_ready():
    print('Logged on as {0}!'.format(discord_client.user))


@discord_client.event
async def on_message(message):
    if message.author == discord_client.user:
        return

    if not message.content or message.content.isspace():
        return

    response = await parser.parse(message)
    if response:
        await message.channel.send(response)


discord_client.run(DISCORD_TOKEN)
