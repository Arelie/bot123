import asyncio
from discord.ext import commands


client = commands.Bot(command_prefix='!*')


@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command(name="*")
@commands.has_permissions(administrator=True)
@asyncio.coroutine
def start(*message2):
    if 'message2' not in locals():
        message = ""
    else:
        message = ""
        for x in message2:
            message = message + x + " "
    while True:
        yield from asyncio.sleep(43200)
        yield from client.say(message)


loop = asyncio.get_event_loop()


@client.command(name="stop")
@commands.has_permissions(administrator=True)
@asyncio.coroutine
def stop():
    while True:
        loop.stop
        loop.close


client.run("MzI1Njg0NjM5MjUzMzk3NTA3.DCb0_A.LFAXgf-cVt0ZfsZFZwT9KqGKbrc") #LegionOW
