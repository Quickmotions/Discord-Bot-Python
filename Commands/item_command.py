item_list = [
    [{'pickaxe': 'Used to mine rocks'}, 'None', {}],
    [{'fishingrod': 'Used to fish'}, 'None', {}],
    [{'TinBoots': 'Gives +2 Defense Skill'}, 'Feet', {'Defense': 2}],
    [{'TinLeggings': 'Gives +2 Defense Skill'}, 'Legs', {'Defense': 2}],
    [{'TinChestplate': 'Gives +2 Defense Skill'}, 'Chest', {'Defense': 2}],
    [{'TinHelmet': 'Gives +2 Defense Skill'}, 'Head', {'Defense': 2}],
    [{'ThiefHelmet': 'Gives +2 Stealing, +2 Agility Skill'}, 'Head', {'Stealing': 2, 'Agility': 2}],
    [{'ThiefChestplate': 'Gives +2 Stealing, +2 Agility Skill'}, 'Chest', {'Stealing': 2, 'Agility': 2}],
    [{'ThiefLeggings': 'Gives +2 Stealing, +2 Agility Skill'}, 'Legs', {'Stealing': 2, 'Agility': 2}],
    [{'ThiefBoots': 'Gives +2 Stealing, +2 Agility Skill'}, 'Feet', {'Stealing': 2, 'Agility': 2}],
    [{'WarriorBoots': 'Gives +2 Combat Skill'}, 'Feet', {'Combat': 2}],
    [{'WarriorLeggings': 'Gives +2 Combat Skill'}, 'Legs', {'Combat': 2}],
    [{'WarriorChestplate': 'Gives +2 Combat Skill'}, 'Chest', {'Combat': 2}],
    [{'WarriorHelmet': 'Gives +2 Combat Skill'}, 'Head', {'Combat': 2}],
    [{'FishBoots': 'Gives +2 Fishing Skill'}, 'Feet', {'Fishing': 2}],
    [{'FishChestplate': 'Gives +2 Fishing Skill'}, 'Chest', {'Fishing': 2}],
    [{'FishLeggings': 'Gives +2 Fishing Skill'}, 'Legs', {'Fishing': 2}],
    [{'FishHelmet': 'Gives +2 Fishing Skill'}, 'Head', {'Fishing': 2}],
    [{'MinerBoots': 'Gives +2 Mining Skill'}, 'Feet', {'Mining': 2}],
    [{'MinerHelmet': 'Gives +2 Mining Skill'}, 'Head', {'Mining': 2}],
    [{'MinerChestplate': 'Gives +2 Mining Skill'}, 'Chest', {'Mining': 2}],
    [{'MinerLeggings': 'Gives +2 Mining Skill'}, 'Legs', {'Mining': 2}],
    [{'IronSword': 'Gives +4 Combat Skill'}, 'Hand', {'Combat': 4}],
    [{'MagicStaff': 'Gives +4 Magic Skill'}, 'Hand', {'Magic': 4}],
    [{'GemFishingRod': 'Gives +5 Fishing Skill'}, 'Hand', {'Fishing': 5}],
    [{'LuckyStick': 'Gives +5 Luck Skill'}, 'Hand', {'Luck': 5}],
    [{'BonerSword': 'Gives +6 Agility Skill'}, 'Hand', {'Agility': 6}],
    [{'CombatChestplate': 'Gives +2 Combat Skill'}, 'Chest', {'Combat': 2}],
    [{'ChampionChestplate': 'Gives +5 Combat Skill'}, 'Chest', {'Combat': 5}],
    [{'WarBornChestplate': 'Gives +10 Combat Skill'}, 'Chest', {'Combat': 10}],
    [{'MagicChestplate': 'Gives +2 Magic Skill'}, 'Chest', {'Magic': 2}],
    [{'ElementalChestplate': 'Gives +5 Magic Skill'}, 'Chest', {'Magic': 5}],
    [{'ArchMageChestplate': 'Gives +10 Magic Skill'}, 'Chest', {'Magic': 10}],
    [{'AncientChestplate': 'Gives +3 Health Skill'}, 'Chest', {'Health': 3}],
    [{'WandOfHealing': 'Gives +4 Healing Skill'}, 'Hand', {'Healing': 3}],
    [{'ElectrumWand': 'Gives +5 Magic Skill'}, 'Hand', {'Magic': 5}],
    [{'Shield': 'Grants 3 shield each turn'}, 'Hand', {}],
    [{'EternalHelmet': 'Gives +5 Defense Skill, +5 Health Skill'}, 'Head', {'Defense': 5, 'Health': 5}],
    [{'EternalChestplate': 'Gives +5 Defense Skill, +5 Health Skill'}, 'Chest', {'Defense': 5, 'Health': 5}],
    [{'EternalLeggings': 'Gives +5 Defense Skill, +5 Health Skill'}, 'Legs', {'Defense': 5, 'Health': 5}],
    [{'EternalBoots': 'Gives +5 Defense Skill, +5 Health Skill'}, 'Feet', {'Defense': 5, 'Health': 5}],
    [{'EternalGuardianShield': 'Gives +15 Defense Skill'}, 'Hand', {'Defense': 15}],
    [{'AssassinsHelmet': 'Gives +3 Agility Skill'}, 'Head', {'Agility': 3}],
    [{'AssassinsChestplate': 'Gives +3 Agility Skill'}, 'Chest', {'Agility': 3}],
    [{'AssassinsLeggings': 'Gives +3 Agility Skill'}, 'Legs', {'Agility': 3}],
    [{'AssassinsBoots': 'Gives +3 Agility Skill'}, 'Feet', {'Agility': 3}],
    [{'HunterRing': 'Gives +1 Combat Skill, +1 Agility Skill, +1 Magic Skill'}, 'Finger', {'Agility': 1, 'Magic': 1, 'Combat': 1}],
    [{'SorcererWand': 'Gives +5 Magic Skill, +2 Defense Skill'}, 'Hand', {'Magic': 5, 'Defense': 2}],
    [{'MagicDagger': 'Gives +3 Magic Skill, +4 Agility Skill'}, 'Hand', {'Magic': 3, 'Agility': 4}],
    [{'DiabloRing': 'Gives +4 Magic Skill'}, 'Ring', {'Magic': 4}],
    [{'InfinityBoots': 'Gives +8 Magic Skill'}, 'Feet', {'Magic': 8}],
    [{'SpectralHelmet': 'Gives +6 Magic Skill'}, 'Head', {'Magic': 6}],
    [{'SpectralChestplate': 'Gives +6 Magic Skill'}, 'Chest', {'Magic': 6}],
    [{'SpectralLeggings': 'Gives +6 Magic Skill'}, 'Legs', {'Magic': 6}],
    [{'SpectralBoots': 'Gives +6 Magic Skill'}, 'Feet', {'Magic': 6}],
    [{'BasaltShield': 'Gives +8 Defense Skill'}, 'Hand', {'Defense': 8}],
    [{'BasaltHelmet': 'Gives +8 Defense Skill, -4 Health Skill'}, 'Head', {'Defense': 8, 'Health': -4}],
    [{'SkeletalChestplate': 'Gives +5 Agility Skill'}, 'Chest', {'Agility': 5}],
    [{'SteelHelmet': 'Gives +4 Combat Skill'}, 'Head', {'Combat': 4}],
    [{'SteelChestplate': 'Gives +4 Combat Skill'}, 'Chest', {'Combat': 4}],
    [{'SteelLeggings': 'Gives +4 Combat Skill'}, 'Legs', {'Combat': 4}],
    [{'SteelBoots': 'Gives +4 Combat Skill'}, 'Feet', {'Combat': 4}],
    [{'DarkBoots': 'Gives +9 Agility Skill'}, 'Feet', {'Agility': 9}],
    [{'AbyssalDagger': 'Gives +3 Agility Skill, +2 Defense Skill'}, 'Feet', {'Agility': 3, 'Defense': 2}],
    [{'AngelHelmet': 'Gives +10 Healing Skill'}, 'Head', {'Healing': 10}],
    [{'AngelChestplate': 'Gives +10 Healing Skill'}, 'Chest', {'Healing': 10}],
    [{'AngelLeggings': 'Gives +10 Healing Skill'}, 'Legs', {'Healing': 10}],
    [{'AngelBoots': 'Gives +10 Healing Skill'}, 'Feet', {'Healing': 10}],
    [{'StaffOfAegis': 'Gives +18 Magic Skill'}, 'Hand', {'Magic': 18}],

]



def item_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        for item, slot, stats in item_list:
            for item_name, desc in item.items():
                if args[3][0] == item_name.lower():
                    return f"Info for {item_name}:\n{desc}"
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