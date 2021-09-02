# bot.py
import discord
from env import env
from datetime import datetime, timedelta

from Commands.update_skills import setup_skills
from command_manager import Commands
from users import run_setup_users
from cooldown_manager import run_setup_cool_down, CoolDowns
from Commands.update_csv import start_update_csv, start_update_cooldown, start_update_events
from events_manager import check_event_response, Events, get_data
from Commands.inv_command import setup_equipment, set_equipment_stats
from Commands.quest_command import setup_quests

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

    for user in USERS:
        setup_skills(user, USERS)
        setup_equipment(user, USERS)
        set_equipment_stats(user, USERS)


@client.event
async def on_message(message):
    if message.author == client.user:  # stops bot responding to its self
        return
    events = get_data()
    # collect some data from message
    user_id = str(message.author.id)
    username = str(message.author).split('#')[0]  # username only
    user_message = str(message.content).lower()
    channel = str(message.channel.name)
    guild = str(message.author.guild.name)

    user_input = user_message.lower().split(' ')
    user_command = user_input[0].lower()
    user_found = False
    event_found = False

    for user in USERS:
        if user.user_id == user_id:
            user_found = True
            # finds the user who inputted command in the user data
            user_data_for_command = user

    for event in events:
        if event.user_id == user_id:
            event_found = True
            # finds the user who inputted command in the user data

    if not user_found:  # user data missing creates new default for user

        from users import Player
        USERS.append(Player(f"{user_id} {username}"))
        setup_skills(USERS)
        start_update_csv(USERS)
    if not event_found:  # user data missing creates new default for user

        events.append(events(f"{user_id} {username}",
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

        start_update_events(events)

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
            response = C.run_command(user_input, user_data_for_command, C, USERS, user_input[1:], events)

    else:  # message not in commands list (responses check)
        response = check_event_response(user_data_for_command, C, USERS, user_input[1:], events, user_input[0])

    # display output
    if response is not None:
        if isinstance(response, list):
            if response[0] == 'no_embed':
                await message.channel.send(f"{response[1]}")
            if response[0] == 'multiple':
                for text in response[1:]:
                    await message.channel.send(f"```yaml\n{text}```")
        else:
            await message.channel.send(f"```yaml\n{response}```")


if __name__ == '__main__':
    client.run(TOKEN)
