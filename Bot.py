# bot.py
import os
import discord
from discord.ext import commands
from env import env
from datetime import datetime, timedelta

from command_manager import Commands
from users import run_setup_users
from cooldown_manager import run_setup_cool_down, CoolDowns
from Commands.update_csv import start_update_csv, start_update_cooldown, start_update_events
from events_manager import check_event_response, Events, get_data

TOKEN = env()
client = discord.Client()

intents = discord.Intents.default()
intents.members = True  # Subscribe to the privileged members intent.

C = Commands()
USERS = run_setup_users()
CDS = run_setup_cool_down()



@client.event
async def on_ready():
    print("logged in as {0.user}\n\n".format(client))


@client.event
async def on_message(message):
    EVENTS = get_data()
    # collect some data from message
    user_id = str(message.author.id)
    username = str(message.author).split('#')[0]  # username only
    user_message = str(message.content).lower()
    channel = str(message.channel.name)
    guild = str(message.author.guild.name)

    if message.author == client.user:  # stops bot responding to its self
        return

    user_input = user_message.lower().split(' ')
    user_command = user_input[0].lower()
    user_found = False
    event_found = False

    for user in USERS:
        if user.user_id == user_id:
            user_found = True
            # finds the user who inputted command in the user data
            user_data_for_command = user

    for event in EVENTS:
        if event.user_id == user_id:
            event_found = True
            # finds the user who inputted command in the user data

    if not user_found:  # user data missing creates new default for user

        from users import Player
        USERS.append(Player(f"{user_id} {username}",
                            "0.0",
                            "{}",
                            "{'Combat': [0, 0, 100], 'Defense': [0, 0, 100], 'Stealing': [0, 0, 100]}",
                            "None 0.0",
                            "None",
                            "{'Slash': 3, 'Defend': 1, 'Charge': 1}"
                            ))
        start_update_csv(USERS)
    if not event_found:  # user data missing creates new default for user

        EVENTS.append(Events(f"{user_id} {username}",
                             "Active=No",
                             "mob_name",
                             "0",
                             "0",
                             "None",
                             "0",
                             "100",
                             "100",
                             "0"
                             ))

        start_update_events(EVENTS)
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
            response = C.run_command(user_input, user_data_for_command, C, USERS, user_input[1:], EVENTS)

    else:  # message not in commands list (responses check)
        response = check_event_response(user_data_for_command, C, USERS, user_input[1:], EVENTS, user_input[0])

    # display output
    if response is not None:
        if isinstance(response, list):
            if response[0] == 'no_embed':
                await message.channel.send(f"{response[1]}")
            if response[0] == 'multiple':
                for text in response[1:]:
                    await message.channel.send(f"```yaml\n{text}```")
        else:
            await message.channel.send(f"```yaml\nDEBUG: {response}```")


if __name__ == '__main__':
    client.run(TOKEN)