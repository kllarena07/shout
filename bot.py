import discord
from dotenv import load_dotenv
from os import getenv

load_dotenv()

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

    print(f'{message.author.name}: {message.content}')

DISCORD_BOT_TOKEN = getenv("DISCORD_BOT_TOKEN")

client.run(DISCORD_BOT_TOKEN)
