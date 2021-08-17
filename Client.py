# bot.py
import os
import discord
from discord.ext import commands
from env import env

TOKEN = env()
client = discord.Client()

intents = discord.Intents.default()
intents.members = True  # Subscribe to the privileged members intent.
bot = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print("logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    user_id = str(message.author)  # id with #1234
    username = user_id.split('#')[0]  # username only
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:  # stops bot responding to its self
        return

    if user_message.lower() == 'hello':
        await message.channel.send(f'Hello {username}')
        return
    # ect...
    # move command_manager here to start code. we also need to set up user data if the user isn't found in the data



client.run(TOKEN)
