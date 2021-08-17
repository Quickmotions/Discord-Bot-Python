# get commands:
from Commands.bal_command import bal_c
from Commands.help_command import help_c
from Commands.give_command import give_c
from Commands.inv_command import inv_c
from Commands.job_command import job_c
from Commands.train_command import train_c
from Commands.agree_command import agree_c


# controls inputted and outputted commands
class Commands:
    def __init__(self):
        self.command_list = {
            "help": help_c,
            "bal": bal_c,
            "give": give_c,
            "inv": inv_c,
            "job": job_c,
            "train": train_c,
            "agree": agree_c
        }

    def run_command(self, name, user_data, c, users, args):
        return self.command_list[name](user_data, c, users, args)


async def start_input(c, users, user_id, message):
    user_input = message.split(' ')
    for user in users:
        if user.user_id == user_id:   # finds the user who inputted command in the user data
            user_data_for_command = user

    if user_input[0] in c.command_list:
        c.run_command(user_input[0], user_data_for_command, c, users, user_input[1:])




    # if user_message.lower() == 'ping':
    #     await message.channel.send(f'pong, {username}')
    #     return


def start(users):
    c = Commands()
    state = 'input'
    while state == 'input':
        start_input(c, users)
