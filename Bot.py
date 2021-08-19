# bot.py
import os
import discord
from discord.ext import commands
from env import env
from datetime import datetime, timedelta

from command_manager import Commands
from users import run_setup_users
from cooldown_manager import run_setup_cool_down, CoolDowns
from Commands.update_csv import start_update_csv, start_update_cooldown
from events_manager import check_event_response, Events

TOKEN = env()
client = discord.Client()

intents = discord.Intents.default()
intents.members = True  # Subscribe to the privileged members intent.

C = Commands()
USERS = run_setup_users()
CDS = run_setup_cool_down()
event_list = []


@client.event
async def on_ready():
    print("logged in as {0.user}\n\n".format(client))


@client.event
async def on_message(message):
    global event_list
    # collect some data from message
    user_id = str(message.author.id)
    username = str(message.author).split('#')[0]  # username only
    user_message = str(message.content).lower()
    channel = str(message.channel.name)
    guild = str(message.author.guild.name)

    if user_id != '877251653760340039':  # wont print its own messages
        print(f'{user_message}\t-({username}: <@!{user_id}>)\t-({channel}, {guild})')

    if message.author == client.user:  # stops bot responding to its self
        return

    user_input = user_message.lower().split(' ')
    user_command = user_input[0].lower()
    user_found = False

    for user in USERS:
        if user.user_id == user_id:
            user_found = True
            # finds the user who inputted command in the user data
            user_data_for_command = user

    if not user_found:  # user data missing creates new default for user

        from users import Player
        USERS.append(Player(f"{user_id} {username}",
                            "0.0",
                            "{}",
                            "{'Combat': [0, 0, 100], 'Defense': [0, 0, 100], 'Stealing': [0, 0, 100]}",
                            "None 0.0",
                            "None",
                            "No"
                            ))

        start_update_csv(USERS)
        await message.channel.send(f"```yaml\n Generated user data for {username}:\nYou can now use the bot.```")

    if user_command in C.command_list:
        if user_found:
            current_datetime = datetime.today()
            for cd in CDS:
                # test if command is on cool down
                if cd.user_id == user_data_for_command.user_id and cd.command == user_input[0]:
                    # test if cool down has come to an end
                    if current_datetime >= cd.cool_down_end:
                        del cd
                    else:  # tell user cool down is in progress
                        await message.channel.send(f"```yaml\n{cd.command} Still on Cool-Down:\n"
                                                   f"Will be done at {cd.cool_down_end}```")
                        return



            # set time for cool down to end
            time_change = timedelta(seconds=int(C.command_list[user_command][1]))
            cool_down_end = current_datetime + time_change

            # add cool down to csv and class
            CDS.append(CoolDowns(cool_down_end, user_command, user_data_for_command.user_id))
            start_update_cooldown(CDS)

            # run the command
            response = C.run_command(user_input, user_data_for_command, C, USERS, user_input[1:], event_list)

    else:  # message not in commands list (responses check)
        response = check_event_response(user_data_for_command, C, USERS, user_input[1:], event_list)

    # display output
    if response is not None:
        if isinstance(response, list):
            if response[0] == 'no_embed':
                await message.channel.send(f"{response[1]}")
            if response[0] == 'multiple':
                for text in response[1:]:
                    await message.channel.send(f"```yaml\n{text}```")
            if response[0] == 'event':
                event_list.append(Events(response[2][0], response[2][1], response[2][2]))
                await message.channel.send(f"```yaml\n{response[1]}```")
        else:
            await message.channel.send(f"```yaml\nLive Dev Bot (pls Ignore):\n{response}```")

if __name__ == '__main__':
    client.run(TOKEN)
