# get commands:
from Commands.bal_command import bal_c
from Commands.help_command import help_c
from Commands.give_command import give_c
from Commands.inv_command import inv_c
from Commands.job_command import job_c, work_c
from Commands.train_command import train_c
from Commands.agree_command import agree_c
from Commands.skill_command import skill_c
from Commands.rob_command import rob_c
from Commands.hunt_command import hunt_c


# controls inputted and outputted commands
class Commands:
    def __init__(self):
        self.command_list = {
            "help": [help_c, 1],
            "bal": [bal_c, 1],
            "give": [give_c, 1],
            "inv": [inv_c, 1],
            "job": [job_c, 1],
            "work": [work_c, 1200],
            "train": [train_c, 1],
            "agree": [agree_c, 1],
            "skill": [skill_c, 1],
            "rob": [rob_c, 1],
            "hunt": [hunt_c, 1]
        }

    def run_command(self, name, user_data, c, users, args):
        return self.command_list[name[0]][0](user_data, c, users, args)


