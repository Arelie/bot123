import discord
import asyncio
from asyncio import async
import async

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!'):
            await asyncio.sleep(5)
            await client.send_message(message.channel, message.content)
            print(message)

client.run("MzEzMzE3MjAyNDgyNjkyMTA2.C_n25Q.Yu2Q2o8DUlIz2nLcH9IpplHHknM")

PAUSE