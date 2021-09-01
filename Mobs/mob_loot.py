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
    [13, 'AngelHelmet', 1, 10],
    [13, 'AngelChestplate', 1, 10],
    [13, 'AngelLeggings', 1, 10],
    [13, 'AngelBoots', 1, 10],
    [13, 'StaffOfAegis', 1, 2],
    [12, 'LavaSword', 1, 50],
    [9, 'InfinityBoots', 1, 30],
    [10, 'InfinityBoots', 1, 80],
    [6, 'SkeletalChestplate', 1, 8],
    [9, 'HallowedHelmet', 1, 5],
    [9, 'HallowedChestplate', 1, 5],
    [9, 'HallowedLeggings', 1, 5],
    [9, 'HallowedBoots', 1, 5],
    [9, 'HallowedSpear', 1, 3],
    [1, 'PunySword', 1, 80],
    [2, 'PunySword', 1, 80],
    [3, 'PunySword', 1, 80],
    [4, 'PunySword', 1, 80],
    [1, 'OldIronChestplate', 1, 100],
    [2, 'OldIronChestplate', 1, 100],
    [3, 'OldIronChestplate', 1, 100],
    [1, 'SlimeRing', 1, 10],
    [7, 'Katana', 2, 90],
    [4, 'Katana', 1, 5],
    [3, 'WarlockLeggings', 1, 10],
    [3, 'WarlockBoots', 1, 10],
    [4, 'WarlockLeggings', 1, 20],
    [4, 'WarlockBoots', 1, 20],
    [5, 'WarlockLeggings', 1, 40],
    [5, 'WarlockBoots', 1, 40],
    [2, 'MagicRing', 1, 120],
    [3, 'MagicRing', 1, 120],
    [4, 'MagicRing', 1, 120],
    [5, 'MagicRing', 1, 120],
    [6, 'MagicRing', 1, 120],
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


