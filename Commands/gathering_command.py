from datetime import datetime
import random
from Commands.update_csv import start_update_csv

fish_list = [
    'Cod',
    'Mackerel',
    'Carp',
    'Trout',
    'Salmon',
    'Catfish',
    'Tuna'
]


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

                fish_gained_total = round(duration_in_hour * 20)
                for _ in range(fish_gained_total):
                    fish_gained[random.choice(fish_list)] += 1

                args[0].gathering = "gathering=no"
                args[0].gathering_time = "None"
                start_update_csv(args[2])
                fish_got_str = "You managed to catch:\n"
                for fish in fish_gained:
                    fish_got_str += f"-{fish_gained[fish]} {fish.title()}\n"
                    if fish.title() not in args[0].inv:  # add item to card list if it doesnt exist
                        args[0].inv[fish.title()] = 0
                    args[0].inv[fish] += fish_gained[fish]

                return ["multiple", f"You fished for {round(duration_in_hour, 2)} hours:", fish_got_str]
            else:
                return f"You have only been fishing for {round(duration_in_hour, 2)} hours:\n" \
                       f"-You need to fish for at least 1 hour"
        return "You are already doing a different type of gathering"
    else:
        return "You must own a fishing rod to fish:\n-Try buying one from the shop"
