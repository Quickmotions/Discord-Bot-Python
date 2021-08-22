import random
from events_manager import start_combat


def hunt_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        if args[3][0] == "list":
            return "All hunting Locations:\n" \
                   "Plains: (level 1)\n" \
                   "Forrest: (level 2)\n" \
                   "Swamp: (level 3)\n" \
                   "Pond: (level 4)\n" \
                   "Grasslands: (level 5)\n" \
                   "Ruins: (level 6)\n" \
                   "China: (level 7)\n" \
                   "Artic: (level 8)\n" \
                   "Savanna: (level 9)\n" \
                   "Russia: (level 10)\n" \
                   "Mountains: (level 11)\n" \
                   "Volcano: (level 12)\n" \



        else:
            if args[0].gathering == "gathering=no":
                if args[3][0] == "plains":
                    difficulty = 1
                elif args[3][0] == "forrest":
                    difficulty = 2
                elif args[3][0] == "swamp":
                    difficulty = 3
                elif args[3][0] == "pond":
                    difficulty = 4
                elif args[3][0] == "grasslands":
                    difficulty = 5
                elif args[3][0] == "ruins":
                    difficulty = 6
                elif args[3][0] == "china":
                    difficulty = 7
                elif args[3][0] == "artic":
                    difficulty = 8
                elif args[3][0] == "savanna":
                    difficulty = 9
                elif args[3][0] == "russia":
                    difficulty = 10
                elif args[3][0] == "mountains":
                    difficulty = 11
                elif args[3][0] == "volcano":
                    difficulty = 12
                else:
                    return "Unknown Location:\nUse 'hunt list' to see locations"
                f = open('mobs.txt', 'r')
                mob_list = []
                for mob in f.readlines():
                    enemy = mob.strip().split(',')
                    mob_list.append(enemy)


                # mob data: 0 = difficulty, 1 = name, 2 = hp, 3 = dmg, 4 = coins dropped

                # loop until random mob is right level
                random_mob = random.choice(mob_list)
                while int(random_mob[0]) != difficulty:
                    random_mob = random.choice(mob_list)
                return start_combat(args[0], args[2], random_mob, 'PVE', args[4])
            else:
                return "You are already doing a different type of gathering"


    else:
        return "Incorrect argument:\nUse 'hunt (list) or (location)'"
