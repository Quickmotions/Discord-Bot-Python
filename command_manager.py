# get commands:
from Commands.bal_command import bal_c
from Commands.help_command import help_c
from Commands.give_command import give_c
from Commands.inv_command import inv_c, equip_c
from Commands.job_command import job_c, work_c
from Commands.train_command import train_c
from Commands.agree_command import agree_c
from Commands.rob_command import rob_c
from Commands.hunt_command import hunt_c
from Commands.source_command import source_c
from Commands.steal_command import steal_c
from Commands.gamble_command import gamble_c
from Commands.card_command import card_c
from Commands.shop_command import shop_c
from Commands.item_command import item_c
from Commands.gathering_command import fish_c, mine_c, woodcut_c, quit_c
from Commands.craft_command import craft_c
from Commands.quest_command import quest_c
from Commands.update_skills import skills_c
from Commands.removal_command import removal_c
from Commands.guild_command import guild_c


# controls inputted and outputted commands
class Commands:
    def __init__(self):
        self.command_list = {
            "help": [help_c, 5],
            "bal": [bal_c, 5],
            "give": [give_c, 5],
            "inv": [inv_c, 1],
            "card": [card_c, 1],
            "item": [item_c, 1],
            "equip": [equip_c, 1],
            "shop": [shop_c, 1],
            "craft": [craft_c, 1],
            "job": [job_c, 1],
            "work": [work_c, 10],
            "train": [train_c, 1],
            "agree": [agree_c, 1],
            "stats": [skills_c, 1],
            "skills": [skills_c, 1],
            "rob": [rob_c, 20000],
            "hunt": [hunt_c, 5],
            "source": [source_c, 60],
            "steal": [steal_c, 60],
            "gamble": [gamble_c, 1],
            "fish": [fish_c, 1],
            "mine": [mine_c, 1],
            "woodcut": [woodcut_c, 1],
            "quit": [quit_c, 5],
            "quest": [quest_c, 1],
            "removal": [removal_c, 1],
            "guild": [guild_c, 1],
        }

    def run_command(self, name, user_data, c, users, args, events):
        return self.command_list[name[0]][0](user_data, c, users, args, events)
