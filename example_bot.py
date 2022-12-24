# This example requires the 'message_content' intent.

import discord
import json

setting_file = open('tubelin_config.json', 'r')
setting = json.load(setting_file)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(setting["bot_token"])
