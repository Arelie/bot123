import asyncio
from discord.ext import commands


client = commands.Bot(command_prefix='!')


@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command(name="start")
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
        yield from asyncio.sleep(2)
        yield from client.say(message)


@client.command(name="stop")
@commands.has_permissions(administrator=True)
@asyncio.coroutine
def stop():
    while True:
        loop.stop
        loop.close


loop = asyncio.get_event_loop()


client.run("MzEzMzE3MjAyNDgyNjkyMTA2.C_n25Q.Yu2Q2o8DUlIz2nLcH9IpplHHknM")


