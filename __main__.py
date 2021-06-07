import discord

import tts
import constants as c

intents = discord.Intents().all()

client = discord.Client(prefix='', intents=intents)

client.run(c.TOKEN)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!tts'):
        await tts.tts_message_controller(client, message)
        return
