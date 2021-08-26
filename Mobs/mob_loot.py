from Commands.update_csv import start_update_csv
import random

loot_table = [
    # mob lvl, item, amount, chance
    [1, 'Leather', 2, 100],
    [2, 'SpruceLog', 1, 50],
    [2, 'OakLog', 1, 50],
    [2, 'PineLog', 1, 50],
    [2, 'BeechLog', 1, 50],
    [2, 'MapleLog', 1, 50],
    [2, 'AshLog', 1, 50],
    [3, 'WaterRune', 1, 30],
    [4, 'Cod', 1, 50],
    [4, 'Mackerel', 1, 50],
    [4, 'Carp', 1, 50],
    [4, 'Trout', 1, 50],
    [4, 'Salmon', 1, 50],
    [4, 'Catfish', 1, 50],
    [4, 'Tuna', 1, 50],
    [5, 'Leather', 6, 60],
    [6, 'Bone', 3, 60],
    [7, 'Paper', 2, 70],
    [8, 'IceRune', 1, 30],
    [9, 'SandRune', 1, 30],
    [10, 'GunPart', 1, 90],
    [11, 'EarthRune', 1, 30],
    [12, 'FireRune', 1, 30],

]


def award_hunt_loot(level: int, user, users):

    loot_gained = []
    for mob_level, item, amount, chance in loot_table:
        if mob_level == int(level):
            if random.randint(1, 100) <= int(chance):
                print("true")
                loot_gained.append([item, amount])
                if item not in user.inv:
                    user.inv[item] = 0
                user.inv[item] += amount
                start_update_csv(users)
                print(loot_gained)
                return loot_gained


