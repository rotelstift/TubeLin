import discord
import json

setting_file = open('settings.json', 'r')
setting = json.load(setting_file)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

tree = discord.app_commands.CommandTree(client)

@tree.command(
    name='tubelin',
    description="ようつべで検索したい単語を入れてね",
    auto_locale_strings=False
)
async def tubelin(ctx:discord.Interaction):
    await ctx.response.send_message('https://youtu.be/-_s6kpwTQdg')


@client.event
async def on_ready():
    await tree.sync()
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(setting["bot_token"])
