import os
import discord
from commands.base import CmdParser


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")  # get discord token from
discord_client = discord.Client()
commands_parser = CmdParser()


@discord_client.event
async def on_ready():
    print(f'Logged on as {discord_client.user}!')


@discord_client.event
async def on_message(message):
    if message.author == discord_client.user or not message.content or message.content.isspace():
        return

    response = await commands_parser.parse(message)
    if not response:
        response = 'Command not found'

    await message.channel.send(response)


discord_client.run(DISCORD_TOKEN)
