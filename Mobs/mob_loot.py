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
    [6, 'DeathLily', 3, 250],
    [2, 'AncientRune', 4, 300],
    [4, 'AncientRune', 4, 300],
    [6, 'AncientRune', 4, 300],
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
    [3, 'WarlockLeggings', 1, 20],
    [3, 'WarlockBoots', 1, 20],
    [4, 'WarlockLeggings', 1, 40],
    [4, 'WarlockBoots', 1, 40],
    [5, 'WarlockLeggings', 1, 80],
    [5, 'WarlockBoots', 1, 80],
    [2, 'MagicRing', 1, 120],
    [3, 'MagicRing', 1, 120],
    [4, 'MagicRing', 1, 120],
    [5, 'MagicRing', 1, 120],
    [6, 'MagicRing', 1, 120],
    [1, 'RemovalSigil', 1, 50],
    [2, 'RemovalSigil', 1, 50],
    [3, 'RemovalSigil', 1, 50],
    [4, 'RemovalSigil', 1, 50],
    [5, 'RemovalSigil', 1, 50],
    [6, 'RemovalSigil', 1, 50],
    [7, 'RemovalSigil', 1, 50],
    [8, 'RemovalSigil', 1, 50],
    [9, 'RemovalSigil', 1, 50],
    [10, 'RemovalSigil', 1, 50],
    [11, 'RemovalSigil', 1, 50],
    [12, 'RemovalSigil', 1, 50],
    [13, 'RemovalSigil', 1, 50],
    [5, 'SteelGreatSword', 1, 20],
    [6, 'SteelGreatSword', 1, 40],
    [7, 'SteelGreatSword', 1, 60],
    [8, 'SteelGreatSword', 1, 80],
    [9, 'SteelGreatSword', 1, 100],
    [1, 'DevilsHorn', 2, 100],
    [3, 'DevilsHorn', 4, 100],
    [5, 'DevilsHorn', 8, 100],
    [7, 'DevilsHorn', 16, 100],
    [9, 'DevilsHorn', 32, 100],
    [2, 'DarkShard', 1, 100],
    [3, 'DarkShard', 1, 100],
    [5, 'DarkShard', 1, 100],
    [6, 'DarkShard', 1, 100],
    [7, 'DarkShard', 1, 100],
    [1, 'Blood', 3, 20],
    [2, 'Blood', 4, 40],
    [3, 'Blood', 2, 80],
    [4, 'Blood', 4, 100],
    [5, 'Blood', 3, 100],
    [6, 'Blood', 4, 100],
    [7, 'Blood', 3, 100],
    [8, 'Blood', 2, 100],
    [9, 'Blood', 3, 100],
    [10, 'Blood', 4, 100],
    [11, 'Blood', 2, 100],
    [12, 'Blood', 4, 100],
    [13, 'Blood', 3, 100],
    [6, 'EternalHelmet', 1, 50],
    [6, 'EternalLeggings', 1, 50],
    [7, 'EternalChestplate', 1, 50],
    [7, 'EternalBoots', 1, 50],
    [6, 'Ectoplasm', 6, 500],
    [12, 'DiabloRing', 1, 250],
    [11, 'GolemHelmet', 1, 70],
    [11, 'GolemChestplate', 1, 70],
    [11, 'GolemLeggings', 1, 70],
    [11, 'GolemBoots', 1, 70],
    [12, 'HellhoundHelmet', 1, 200],
    [12, 'HellhoundChestplate', 1, 200],
    [12, 'HellhoundLeggings', 1, 200],
    [12, 'HellhoundBoots', 1, 200],



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
    print(loot_gained)
    return loot_gained


