import os
import discord
from rankbot.commands.base import CmdParser

text = ' '
split = text.split()
text.isspace()

assert text.isspace()

cmd = split[0]
data = split[1:]
print(cmd)
print(data)

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")  # get discord token from
discord_client = discord.Client()
parser = CmdParser()


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
