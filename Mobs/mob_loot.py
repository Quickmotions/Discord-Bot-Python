from Commands.update_csv import start_update_csv
import random

loot_table = [
    # mob lvl, item, amount, chance
    [1, 'Leather', 2, 600],
    [2, 'SpruceLog', 1, 500],
    [2, 'OakLog', 1, 500],
    [2, 'PineLog', 1, 500],
    [2, 'BeechLog', 1, 500],
    [2, 'MapleLog', 1, 500],
    [2, 'AshLog', 1, 500],
    [3, 'WaterRune', 1, 600],
    [4, 'Cod', 1, 500],
    [4, 'Mackerel', 1, 500],
    [4, 'Carp', 1, 500],
    [4, 'Trout', 1, 500],
    [4, 'Salmon', 1, 500],
    [4, 'Catfish', 1, 500],
    [4, 'Tuna', 1, 500],
    [5, 'Leather', 6, 600],
    [6, 'Bone', 3, 600],
    [7, 'Paper', 2, 700],
    [8, 'IceRune', 1, 500],
    [9, 'SandRune', 1, 400],
    [10, 'GunPart', 1, 900],
    [11, 'EarthRune', 1, 300],
    [12, 'FireRune', 1, 300],
    [3, 'AncientChestplate', 1, 10],
    [4, 'AncientChestplate', 1, 20],
    [5, 'AncientChestplate', 1, 30],
    [6, 'AncientChestplate', 1, 40],
    [6, 'WandOfHealing', 1, 50],
    [7, 'WandOfHealing', 1, 80],
    [5, 'ElectrumWand', 1, 10],
    [6, 'ElectrumWand', 1, 15],
    [7, 'ElectrumWand', 1, 20],
    [8, 'ElectrumWand', 1, 30],
    [9, 'ElectrumWand', 1, 50],
    [3, 'AbyssalDagger', 1, 50],
    [5, 'AbyssalDagger', 1, 50],
    [6, 'AbyssalDagger', 1, 50],
    [8, 'BasaltHelmet', 1, 70],
    [14, 'AngelHelmet', 1, 10],
    [14, 'AngelChestplate', 1, 10],
    [14, 'AngelLeggings', 1, 10],
    [14, 'AngelBoots', 1, 10],
    [14, 'StaffOfAegis', 1, 2],

]


def award_hunt_loot(level: int, user, users):

    loot_gained = []
    for mob_level, item, amount, chance in loot_table:
        if mob_level == int(level):
            if random.randint(1, 1000) <= int(chance):
                loot_gained.append([item, amount])
                if item not in user.inv:
                    user.inv[item] = 0
                user.inv[item] += amount
                start_update_csv(users)
                return loot_gained


