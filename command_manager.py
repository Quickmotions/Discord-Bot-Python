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
from Commands.source_command import source_c
from Commands.steal_command import steal_c
from Commands.gamble_command import gamble_c
from Commands.card_command import card_c
from Commands.shop_command import shop_c
from Commands.item_command import item_c
from Commands.gathering_command import fish_c, mine_c


# controls inputted and outputted commands
class Commands:
    def __init__(self):
        self.command_list = {
            "help": [help_c, 10],
            "bal": [bal_c, 5],
            "give": [give_c, 5],
            "inv": [inv_c, 5],
            "card": [card_c, 2],
            "item": [item_c, 2],
            "shop": [shop_c, 3],
            "job": [job_c, 3],
            "work": [work_c, 5],
            "train": [train_c, 1],
            "agree": [agree_c, 1],
            "skill": [skill_c, 5],
            "rob": [rob_c, 72000],
            "hunt": [hunt_c, 10],
            "source": [source_c, 3],
            "steal": [steal_c, 60],
            "gamble": [gamble_c, 5],
            "fish": [fish_c, 5],
            "mine": [mine_c, 5]
        }

    def run_command(self, name, user_data, c, users, args, events):
        return self.command_list[name[0]][0](user_data, c, users, args, events)
