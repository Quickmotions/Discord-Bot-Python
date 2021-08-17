# bot.py
import os
import discord
from discord.ext import commands
from env import env

from command_manager import start_input, Commands
from users import run_setup

TOKEN = env()
client = discord.Client()

intents = discord.Intents.default()
intents.members = True  # Subscribe to the privileged members intent.
bot = commands.Bot(command_prefix='!', intents=intents)

C = Commands()
USERS = run_setup()

@client.event
async def on_ready():
    print("logged in as {0.user}".format(client))
    for user in USERS:
        print(user.user_id)

@client.event
async def on_message(message):
    user_id = str(message.author.id)
    username = str(message.author).split('#')[0]  # username only
    user_message = str(message.content).lower()
    channel = str(message.channel.name)
    print(f'{user_id}: {username}: {user_message} ({channel})')  # logs messages

    if message.author == client.user:  # stops bot responding to its self
        return

    user_input = user_message.split(' ')
    user_found = False

    for user in USERS:
        if user.user_id == user_id:
            user_found = True
            # finds the user who inputted command in the user data
            user_data_for_command = user

    if not user_found: # user data missing creates new default for user
        from Commands.update_csv import start_update_csv
        from users import Player
        USERS.append(Player(f"{user_id} {username}",
                            "0.0",
                            "{}",
                            "{'Combat': [0, 0, 100], 'Defense': [0, 0, 100], 'Thievery': [0, 0, 100]}",
                            "None 0.0"
                            ))

        start_update_csv(USERS)

    if user_input[0] in C.command_list:
        response = C.run_command(user_input[0], user_data_for_command, C, USERS, user_input[1:])
        if isinstance(response, list):
            await message.channel.send(f"{response[0]}")
        else:
            if response is not None:
                await message.channel.send(f"```yaml\n{response}```")

# if user_message.lower() == 'ping':
#     await message.channel.send(f'pong, {username}')
#     return
    # ect...
    # move command_manager here to start code. we also need to set up user data if the user isn't found in the data


client.run(TOKEN)
