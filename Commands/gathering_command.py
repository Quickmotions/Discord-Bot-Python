from datetime import datetime
import random
from Commands.update_csv import start_update_csv
from Commands.update_skills import give_xp

fish_list = [
    'Cod',
    'Mackerel',
    'Carp',
    'Trout',
    'Salmon',
    'Catfish',
    'Tuna'
]

mine_list = [
    'Stone',
    'Stone',
    'Stone',
    'Limestone',
    'Limestone',
    'Basalt',
    'Basalt',
    'Ironore',
    'Ironore',
    'Ironore',
    'Goldore',
    'Goldore',
    'Tinore',
    'Tinore',
    'Tinore',
    'Ruby',
    'Sapphire',
    'Diamond',
    'Mithrilore',
    'Obsidian',
    'Obsidian',
    'Titaniumore'

]

woodcut_list = [
    'OakLog',
    'SpruceLog',
    'PineLog',
    'BeechLog',
    'MapleLog',
    'AshLog'
]


def quit_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if args[0].gathering != "gathering=no":
        args[0].gathering = "gathering=no"
        args[0].gathering_time = "None"
        start_update_csv(args[2])
        return "You quit your gathering, and got nothing, lol."


def fish_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if 'Fishingrod' in args[0].inv:
        if args[0].gathering == "gathering=no":
            args[0].gathering = "gathering=fishing"
            args[0].gathering_time = datetime.today()
            start_update_csv(args[2])
            return "Started fishing:\nYou can finnish Fishing in 1 hour or more by typing 'fish' again\n" \
                   "You may not do another type of gathering or hunting while fishing"
        if args[0].gathering == "gathering=fishing":
            current_time = datetime.today()
            duration = current_time - args[0].gathering_time
            duration_in_sec = duration.total_seconds()
            duration_in_hour = duration_in_sec / 60 / 60
            if duration_in_hour > 1.0:
                fish_gained = {'Cod': 0,
                               'Mackerel': 0,
                               'Carp': 0,
                               'Trout': 0,
                               'Salmon': 0,
                               'Catfish': 0,
                               'Tuna': 0}

                if 'Fishing' not in args[0].skills:
                    args[0].skills['Fishing'] = [0, 0, 100]
                fish_gained_total = round(
                    duration_in_hour * (20 + (2 * (args[0].skills['Fishing'][0] + args[0].equipment_stats['Fishing']))))
                for _ in range(fish_gained_total):
                    fish_gained[random.choice(fish_list)] += 1

                args[0].gathering = "gathering=no"
                args[0].gathering_time = "None"

                fish_got_str = "You managed to gather:\n"
                for fish in fish_gained:
                    fish_got_str += f"-{fish_gained[fish]} {fish}\n"
                    if fish not in args[0].inv:  # add item to card list if it doesnt exist
                        args[0].inv[fish] = 0
                    args[0].inv[fish] += fish_gained[fish]
                if 'Fishing' not in args[0].skills:
                    args[0].skills['Fishing'] = [0, 0, 100]
                xp_got = round(duration_in_hour * random.randint(90, 100))
                give_xp(xp_got, "Fishing", args[0], args[2])
                tp_earned = round(duration_in_hour * 1.2)
                # adds TrainingPoints to inv if the user has never had any
                if 'TrainingPoint' not in args[0].inv:
                    args[0].inv['TrainingPoint'] = 0
                args[0].inv['TrainingPoint'] += tp_earned

                start_update_csv(args[2])
                return ["multiple",
                        f"You fished for {round(duration_in_hour, 2)} hours:\nYou got {xp_got} Fishing xp and {tp_earned} TrainingPoints.",
                        fish_got_str]
            else:
                return f"You have only been fishing for {round(duration_in_hour, 2)} hours:\n" \
                       f"-You need to fish for at least 1 hour"
        return "You are already doing a different type of gathering, type 'quit' to cancel gathering."
    else:
        return "You must own a fishing rod to fish:\n-Try buying one from the shop"


def mine_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if 'Pickaxe' in args[0].inv:
        if args[0].gathering == "gathering=no":
            args[0].gathering = "gathering=mining"
            args[0].gathering_time = datetime.today()
            start_update_csv(args[2])
            return "Started mining:\nYou can finnish Mining in 1 hour or more by typing 'mine' again\n" \
                   "You may not do another type of gathering or hunting while mining"
        if args[0].gathering == "gathering=mining":
            current_time = datetime.today()
            duration = current_time - args[0].gathering_time
            duration_in_sec = duration.total_seconds()
            duration_in_hour = duration_in_sec / 60 / 60
            if duration_in_hour > 1.0:
                mine_gained = {'Stone': 0,
                               'Limestone': 0,
                               'Basalt': 0,
                               'Ironore': 0,
                               'Goldore': 0,
                               'Tinore': 0,
                               'Ruby': 0,
                               'Sapphire': 0,
                               'Diamond': 0,
                               'Mithrilore': 0,
                               'Obsidian': 0,
                               'Titaniumore': 0,
                               }

                if 'Mining' not in args[0].skills:
                    args[0].skills['Mining'] = [0, 0, 100]
                mine_gained_total = round(
                    duration_in_hour * (20 + (2 * (args[0].skills['Mining'][0] + args[0].equipment_stats['Mining']))))
                for _ in range(mine_gained_total):
                    mine_gained[random.choice(mine_list)] += 1

                args[0].gathering = "gathering=no"
                args[0].gathering_time = "None"

                mine_got_str = "You managed to gather:\n"
                for mine in mine_gained:
                    mine_got_str += f"-{mine_gained[mine]} {mine}\n"
                    if mine not in args[0].inv:  # add item to card list if it doesnt exist
                        args[0].inv[mine] = 0
                    args[0].inv[mine] += mine_gained[mine]
                if 'Mining' not in args[0].skills:
                    args[0].skills['Mining'] = [0, 0, 100]
                xp_got = round(duration_in_hour * random.randint(90, 100))
                give_xp(xp_got, "Mining", args[0], args[2])
                tp_earned = round(duration_in_hour * 1.2)
                # adds TrainingPoints to inv if the user has never had any
                if 'TrainingPoint' not in args[0].inv:
                    args[0].inv['TrainingPoint'] = 0
                args[0].inv['TrainingPoint'] += tp_earned

                start_update_csv(args[2])
                return ["multiple",
                        f"You Mined for {round(duration_in_hour, 2)} hours:\nYou got {xp_got} Mining xp and {tp_earned} TrainingPoints.",
                        mine_got_str]
            else:
                return f"You have only been Mining for {round(duration_in_hour, 2)} hours:\n" \
                       f"-You need to Mine for at least 1 hour"
        return "You are already doing a different type of gathering, type 'quit' to cancel gathering."
    else:
        return "You must own a Pickaxe to mine:\n-Try buying one from the shop"


def woodcut_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if 'Axe' in args[0].inv:
        if args[0].gathering == "gathering=no":
            args[0].gathering = "gathering=woodcut"
            args[0].gathering_time = datetime.today()
            start_update_csv(args[2])
            return "Started cutting wood:\nYou can finnish cutting wood in 1 hour or more by typing 'woodcut' again\n" \
                   "You may not do another type of gathering or hunting while cutting wood"
        if args[0].gathering == "gathering=woodcut":
            current_time = datetime.today()
            duration = current_time - args[0].gathering_time
            duration_in_sec = duration.total_seconds()
            duration_in_hour = duration_in_sec / 60 / 60
            if duration_in_hour > 1.0:
                wood_gained = {'OakLog': 0,
                               'SpruceLog': 0,
                               'PineLog': 0,
                               'BeechLog': 0,
                               'MapleLog': 0,
                               'AshLog': 0
                               }

                if 'Woodcut' not in args[0].skills:
                    args[0].skills['Woodcut'] = [0, 0, 100]
                wood_gained_total = round(
                    duration_in_hour * (20 + (2 * (args[0].skills['Woodcut'][0] + args[0].equipment_stats['Woodcut']))))
                for _ in range(wood_gained_total):
                    wood_gained[random.choice(woodcut_list)] += 1

                args[0].gathering = "gathering=no"
                args[0].gathering_time = "None"

                wood_got_str = "You managed to gather:\n"
                for wood in wood_gained:
                    wood_got_str += f"-{wood_gained[wood]} {wood}\n"
                    if wood not in args[0].inv:  # add item to card list if it doesnt exist
                        args[0].inv[wood] = 0
                    args[0].inv[wood] += wood_gained[wood]
                if 'Woodcut' not in args[0].skills:
                    args[0].skills['Woodcut'] = [0, 0, 100]
                xp_got = round(duration_in_hour * random.randint(90, 100))
                give_xp(xp_got, "Woodcut", args[0], args[2])
                tp_earned = round(duration_in_hour * 1.2)
                # adds TrainingPoints to inv if the user has never had any
                if 'TrainingPoint' not in args[0].inv:
                    args[0].inv['TrainingPoint'] = 0
                args[0].inv['TrainingPoint'] += tp_earned

                start_update_csv(args[2])
                return ["multiple",
                        f"You cut wood for {round(duration_in_hour, 2)} hours:\nYou got {xp_got} Woodcut xp and {tp_earned} TrainingPoints.",
                        wood_got_str]
            else:
                return f"You have only been cutting wood for {round(duration_in_hour, 2)} hours:\n" \
                       f"-You need to cut wood for at least 1 hour"
        return "You are already doing a different type of gathering, type 'quit' to cancel gathering."
    else:
        return "You must own a Axe to cut wood:\n-Try buying one from the shop"
