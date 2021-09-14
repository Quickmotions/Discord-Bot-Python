import random
from events_manager import start_combat

# LEVEL RULES:
# lvl, name, hp, dmg, item skill points avg
# 1-Plains - 15 - 5 Drops: 4
# 2-Forrest - 35 - 8 Drops: 6
# 3-Swamp - 90 - 15 Drops: 10
# 4-Pond - 150 - 30 Drops: 12
# 5-Grasslands - 220 - 40 Drops: 16
# 6-Ruins - 350 - 60 Drops: 18
# 7-Catacombs  - 420 - 75 Drops: 20
# 8-China - 550 - 100 Drops: 23
# 9-Savannah - 700 - 120 Drops: 25
# 10-Arctic - 840 - 150 Drops: 26
# 11-Jungle  - 1000 - 160 Drops: 28
# 12-Graveyard- 1200 - 160 Drops: 30
# 13-Russia - 1300 - 170 Drops: 32
# 14-Cave- 1550 - 180 Drops: 35
# 15-Egypt - 1800 - 200 Drops: 38
# 16-Atlantis- 2400 - 220 Drops: 40
# 17-Mountains - 2800 - 275 Drops: 45
# 18-Voidzone - 4000 - 300 Drops: 48
# 19-Volcano - 10000 - 400 Drops: 50
# 20-Heaven  - 15000 - 700 Drops: 60
# 21-Hell - 30000 - 1000 Drops: 75


stats = {
    # lvl : [hp, dmg, loot]
    1:  [15, 5, 10],
    2: [35, 8, 15],
    3: [90, 15, 25],
    4: [150, 30, 40],
    5: [220, 40, 75],
    6: [350, 60, 105],
    7: [420, 75, 140],
    8: [550, 100, 190],
    9: [700, 120, 230],
    10: [840, 150, 260],
    11: [1000, 160, 300],
    12: [1200, 160, 340],
    13: [1300, 180, 360],
    14: [1550, 180, 400],
    15: [1800, 200, 450],
    16: [2400, 220, 510],
    17: [2700, 275, 590],
    18: [4000, 300, 700],
    19: [10000, 400, 1000],
    20: [15000, 700, 4000],
    21: [30000, 1000, 20000],
    101: [800, 150, 50]
}



def hunt_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        if args[3][0] == "list":
            return "All hunting Locations:\n" \
                   "Plains-------(level 1)\n" \
                   "Forrest------(level 2)\n" \
                   "Swamp-------(level 3)\n" \
                   "Pond---------(level 4)\n" \
                   "Grasslands--(level 5)\n" \
                   "Ruins--------(level 6)\n" \
                   "Catacombs--(level 7)\n" \
                   "China--------(level 8)\n" \
                   "Savannah----(level 9)\n" \
                   "Arctic-------(level 10)\n" \
                   "Jungle-------(level 11)\n" \
                   "Graveyard---(level 12)\n" \
                   "Russia-------(level 13)\n" \
                   "Cave---------(level 14)\n" \
                   "Egypt--------(level 15)\n" \
                   "Atlantis-----(level 16)\n" \
                   "Mountains--(level 17)\n" \
                   "Voidzone----(level 18)\n" \
                   "Volcano-----(level 19)\n" \
                   "Heaven------(level 20)\n" \
                   "Hell---------(level 21)\n" \
                    "Elemental---(special level)"
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
                elif args[3][0] == "catacombs":
                    difficulty = 7
                elif args[3][0] == "china":
                    difficulty = 8
                elif args[3][0] == "savannah":
                    difficulty = 9
                elif args[3][0] == "arctic":
                    difficulty = 10
                elif args[3][0] == "jungle":
                    difficulty = 11
                elif args[3][0] == "graveyard":
                    difficulty = 12
                elif args[3][0] == "russia":
                    difficulty = 13
                elif args[3][0] == "cave":
                    difficulty = 14
                elif args[3][0] == "egypt":
                    difficulty = 15
                elif args[3][0] == "atlantis":
                    difficulty = 16
                elif args[3][0] == "mountains":
                    difficulty = 17
                elif args[3][0] == "voidzone":
                    difficulty = 18
                elif args[3][0] == "volcano":
                    difficulty = 19
                elif args[3][0] == "heaven":
                    difficulty = 20
                elif args[3][0] == "hell":
                    difficulty = 21
                elif args[3][0] == "elemental":
                    difficulty = 101
                else:
                    return "Unknown Location:\nUse 'hunt list' to see locations"
                f = open('Mobs/mobs.txt', 'r')
                mob_list = []
                for mob in f.readlines():
                    enemy = mob.strip().split(',')
                    mob_list.append(enemy)

                # loop until random mob is right level
                random_mob = random.choice(mob_list)

                while int(random_mob[0]) != difficulty:
                    random_mob = random.choice(mob_list)

                # sets all stats with factor of -0.3 to 0.3 of the stats for that difficulty
                name = random_mob[1]
                hp = round(stats[difficulty][0] * (1 + (0.05 * random.randrange(-1, 1))))
                dmg = round(stats[difficulty][1] * (1 + (0.05 * random.randrange(-1, 1))))
                loot = round(stats[difficulty][2] * (1 + (0.05 * random.randrange(-1, 1))))

                mob_data = [difficulty, name, hp, dmg, loot]

                return start_combat(args[0], args[2], mob_data, 'PVE', args[4])
            else:
                return "You are already doing a different type of gathering"


    else:
        return "Incorrect argument:\nUse 'hunt (list) or (location)'"
