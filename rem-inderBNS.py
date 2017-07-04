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


@client.command(name="message")
@commands.has_permissions(administrator=True)
@asyncio.coroutine
def message():
    while True:
        yield from asyncio.sleep(43200)
        yield from client.say('Make sure to register on time for our tournaments every saturday at:' + '\n' + 'https://www.legionesports.com/events/' + '\n'
                          + '\n' + 'Also Legion Esports T-shirt are here!' + '\n' + 'https://cdn.discordapp.com/attachments/269220781710376960/331128635681406976/3d_design.jpg'
                          + '\n' + '\n' + 'Pre-order can be made at' + '\n' + 'Thimo@legionesports.com' + '\n' + 'First edition sales starts at €34,99. If we hit a good amount of orders. People who pre ordered already get a discount.'
                          + '\n' + 'For more info you can message anyone in Legion Esports trough Discord.')


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


client.run("MzIwMjY0OTY4NzIzMjM0ODE3.DCb29Q.yMbOB8e84h1vGoD2O-DCtwbqy6A") #LegionBNS
