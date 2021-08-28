item_list = {
    'pickaxe': 'Used to mine rocks',
    'fishingrod': 'Used to fish',
    'TinBoots': 'Gives +2 Defense Skill',
    'TinLeggings': 'Gives +2 Defense Skill',
    'TinChestplate': 'Gives +2 Defense Skill',
    'TinHelmet': 'Gives +2 Defense Skill',
    'ThiefHelmet': 'Gives +2 Stealing, +2 Agility Skill',
    'ThiefChestplate': 'Gives +2 Stealing, +2 Agility Skill',
    'ThiefLeggings': 'Gives +2 Stealing, +2 Agility Skill',
    'ThiefBoots': 'Gives +2 Stealing, +2 Agility Skill',
    'WarriorBoots': 'Gives +2 Combat Skill',
    'WarriorLeggings': 'Gives +2 Combat Skill',
    'WarriorChestplate': 'Gives +2 Combat Skill',
    'WarriorHelmet': 'Gives +2 Combat Skill',
    'FishBoots': 'Gives +2 Fishing Skill',
    'FishChestplate': 'Gives +2 Fishing Skill',
    'FishLeggings': 'Gives +2 Fishing Skill',
    'FishHelmet': 'Gives +2 Fishing Skill',
    'MinerBoots': 'Gives +2 Mining Skill',
    'MinerHelmet': 'Gives +2 Mining Skill',
    'MinerChestplate': 'Gives +2 Mining Skill',
    'MinerLeggings': 'Gives +2 Mining Skill',
    'IronSword': 'Gives +4 Combat Skill',
    'MagicStaff': 'Gives +4 Magic Skill',
    'GemFishingRod': 'Gives +5 Fishing Skill',
    'LuckyStick': 'Gives +5 Luck Skill',
    'BonerSword': 'Gives +6 Agility Skill',
    '1WarBornChestplate': 'Gives +2 Combat Skill',
    '2WarBornChestplate': 'Gives +5 Combat Skill',
    '3WarBornChestplate': 'Gives +10 Combat Skill',
    '1MagicChestplate': 'Gives +2 Magic Skill',
    '2MagicChestplate': 'Gives +5 Magic Skill',
    '3MagicChestplate': 'Gives +10 Magic Skill',
    'AncientChestplate': 'Gives +3 Health Skill',
    'WandOfHealing': 'Gives +4 Healing Skill',

}


def item_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        for item in item_list:
            if args[3][0] == item.lower():
                return f"Info for {item}:\n{item_list[item]}"
    else:
        return f"Incorrect use of item:\ntry 'item (item-name)'"


# def use_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
#     if len(args[3]) > 0:
#         if args[3][0] == "removalsigil":
#             if len(args[3]) > 1:
#
#
#     else:
#         return "Incorrect use of 'use':\nTry 'use (item)'"