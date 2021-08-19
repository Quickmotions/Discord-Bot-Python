import random
from events_manager import start_combat

def hunt_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        if args[3][0] == "list":
            return ["multiple",
                    "All hunting Locations:",
                    "Plains: (easy)",
                    "Swamp: (medium)",
                    "Mountains: (hard)",
                    "Volcano: (pog)"]

        else:
            if args[3][0] == "plains":
                difficulty = 1
            elif args[3][0] == "swamp":
                difficulty = 2
            elif args[3][0] == "mountains":
                difficulty = 3
            elif args[3][0] == "volcano":
                difficulty = 4
            else:
                return "Unknown Location:\nUse 'hunt list' to see locations"
            f = open('mobs.txt', 'r')
            mob_list = []
            for mob in f.readlines():
                enemy = mob.strip().split(',')
                mob_list.append(enemy)

            # mob data: 0 = difficulty, 1 = name, 2 = hp, 3 = dmg

            # loop until random mob is right level
            random_mob = random.choice(mob_list)
            while int(random_mob[0]) != difficulty:
                random_mob = random.choice(mob_list)
            return start_combat(args[0], args[2], random_mob, 'PVE', args[4])


    else:
        return "Incorrect argument:\nUse 'hunt (list) or (location)'"
