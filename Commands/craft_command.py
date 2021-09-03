from Commands.update_csv import start_update_csv
from Commands.item_command import item_list

craft_list = {
    'IronIngot': [{'Ironore': 2}, {'Coal': 1}],
    'TinIngot': [{'Tinore': 2}, {'Coal': 1}],
    'GoldIngot': [{'Goldore': 2}, {'Coal': 1}],
    'MithrilIngot': [{'Mithrilore': 3}, {'Coal': 10}],
    'TitaniumIngot': [{'Titaniumore': 3}, {'Coal': 10}],
    'FishIngot': [{'Cod': 10}, {'Tuna': 10}, {'Catfish': 10}, {'Trout': 10}, {'Carp': 10}, {'Mackerel': 10},
                  {'Salmon': 10}],
    'GemIngot': [{'Ruby': 10}, {'Sapphire': 10}, {'Diamond': 10}],
    'CutStone': [{'Stone': 2}],
    'CutLimestone': [{'Limestone': 2}],
    'CutBasalt': [{'Basalt': 2}],
    'Paper': [{'OakLog': 4}],
    'BloodInfusedStone': [{'Blood': 1, 'CutStone': 2}],
    'BloodInfusedIngot': [{'Blood': 1, 'IronIngot': 2}],
    'BloodInfusedDiamond': [{'Blood': 10, 'Diamond': 1}],
    'DevilIngot': [{'DevilsHorn': 1, 'Tinore': 1, 'Coal': 10}],

    'RemovalSigil': [{'CutStone': 20}, {'Paper': 20}, {'WaterRune': 5}, {'MapleLog': 20}],
    'FishMeal': [{'Cod': 15}, {'Tuna': 15}, {'Catfish': 15}, {'Trout': 5}],
    'FishSoup': [{'Carp': 10}, {'Mackerel': 10}, {'Salmon': 10}, {'Trout': 5}],
    'TinHelmet': [{'TinIngot': 25}],
    'TinChestplate': [{'TinIngot': 40}],
    'TinLeggings': [{'TinIngot': 35}],
    'TinBoots': [{'TinIngot': 20}],
    'ThiefHelmet': [{'GoldIngot': 10}, {'Leather': 40}],
    'ThiefChestplate': [{'GoldIngot': 20}, {'Leather': 40}],
    'ThiefLeggings': [{'GoldIngot': 15}, {'Leather': 40}],
    'ThiefBoots': [{'GoldIngot': 10}, {'Leather': 40}],
    'WarriorHelmet': [{'IronIngot': 30}, {'Ruby': 20}],
    'WarriorChestplate': [{'IronIngot': 30}, {'Ruby': 20}],
    'WarriorLeggings': [{'IronIngot': 30}, {'Ruby': 20}],
    'WarriorBoots': [{'IronIngot': 30}, {'Ruby': 20}],
    'CombatChestplate': [{'TinIngot': 50}, {'IronIngot': 50}],
    'ChampionChestplate': [{'CombatChestplate': 1}, {'Bone': 200}],
    'WarBornChestplate': [{'ChampionChestplate': 1}, {'Leather': 200}, {'GoldIngot': 200}, {'GemIngot': 40}],
    'MagicChestplate': [{'Paper': 50}, {'Leather': 50}],
    'ElementalChestplate': [{'MagicChestplate': 1}, {'WaterRune': 75}],
    'ArchMageChestplate': [{'ElementalChestplate': 1}, {'IceRune': 100}, {'EarthRune': 200}, {'SandRune': 40}],
    'FishHelmet': [{'FishIngot': 20}],
    'FishChestplate': [{'FishIngot': 20}],
    'FishLeggings': [{'FishIngot': 20}],
    'FishBoots': [{'FishIngot': 20}],
    'MinerHelmet': [{'GemIngot': 15}],
    'MinerChestplate': [{'GemIngot': 20}],
    'MinerLeggings': [{'GemIngot': 20}],
    'MinerBoots': [{'GemIngot': 20}],
    'BonerSword': [{'Bone': 150}],
    'IronSword': [{'IronIngot': 80}],
    'MagicStaff': [{'GoldIngot': 60}],
    'GemFishingRod': [{'GemIngot': 20}],
    'LuckyStick': [{'GemIngot': 20}],
    'Shield': [{'IronIngot': 150}],
    'BasaltShield': [{'CutBasalt': 250}],
    'BasaltHelmet': [{'CutBasalt': 150, 'Ruby': 60, 'BlackLeather': 20}],
    'SkeletalChestplate': [{'Bone': 420}],
    'SteelHelmet': [{'IronIngot': 60, 'Coal': 60}],
    'SteelChestplate': [{'IronIngot': 60, 'Coal': 60}],
    'SteelLeggings': [{'IronIngot': 60, 'Coal': 60}],
    'SteelBoots': [{'IronIngot': 60, 'Coal': 60}],
    'SteelGreatSword': [{'IronIngot': 95, 'Coal': 95}],
    'DarkBoots': [{'BlackLeather': 300, 'ShadeWoodLog': 100}],
    'KnightHelmet': [{'MithrilIngot': 40}],
    'KnightChestplate': [{'MithrilIngot': 40}],
    'KnightLeggings': [{'MithrilIngot': 40}],
    'KnightBoots': [{'MithrilIngot': 40}],
    'DarkKnightHelmet': [{'KnightHelmet': 1, 'TitaniumIngot': 40, 'DarkShard': 5}],
    'DarkKnightChestplate': [{'KnightChestplate': 1, 'TitaniumIngot': 40, 'DarkShard': 5}],
    'DarkKnightLeggings': [{'KnightLeggings': 1, 'TitaniumIngot': 40, 'DarkShard': 5}],
    'DarkKnightBoots': [{'KnightBoots': 1, 'TitaniumIngot': 40, 'DarkShard': 5}],
    'SpectralHelmet': [{'Ectoplasm': 500, 'BloodInfusedDiamond': 5, 'Crystalium': 100}],
    'SpectralChestplate': [{'Ectoplasm': 500, 'BloodInfusedDiamond': 5, 'Crystalium': 100}],
    'SpectralLeggings': [{'Ectoplasm': 500, 'BloodInfusedDiamond': 5, 'Crystalium': 100}],
    'SpectralBoots': [{'Ectoplasm': 500, 'BloodInfusedDiamond': 5, 'Crystalium': 100}],
    'CursedMask': [{'Coal': 1000, 'BloodInfusedIngot': 10}],
    'GriffinHelmet': [{'ShadeWoodLog': 60, 'Obsidian': 100, 'Crystalium': 60, 'DevilsHorn': 40}],
    'GriffinChestplate': [{'ShadeWoodLog': 60, 'Obsidian': 100, 'Crystalium': 60, 'DevilsHorn': 40}],
    'GriffinLeggings': [{'ShadeWoodLog': 60, 'Obsidian': 100, 'Crystalium': 60, 'DevilsHorn': 40}],
    'GriffinBoots': [{'ShadeWoodLog': 60, 'Obsidian': 100, 'Crystalium': 60, 'DevilsHorn': 40}],
    'Wrath': [{'Blood': 40, 'Paper': 25}],
    'FrostArrow': [{'Crystalium': 20, 'DevilsHorn': 15}],
    'Corruption': [{'BlackLeather': 30, 'Obsidian': 10}],
    'Evasion': [{'AncientRune': 40, 'Sapphire': 80}],
    'Shockwave': [{'AncientRune': 40, 'DevilIngot': 10}],

    'TrainingPoint': [{'Diamond': 1}, {'Ruby': 1}, {'Trout': 3}, {'Catfish': 3}],

}


def craft_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        for craftable in craft_list:
            if args[3][0] == craftable.lower() or args[3][0] == craftable:
                # check for components
                for component in craft_list[craftable]:

                    amount = 1
                    if len(args[3]) > 1:
                        amount = int(args[3][1])

                    for item, quantity in component.items():
                        if item not in args[0].inv:
                            return f"{args[0].username}, You do not own {quantity * amount} {item}(s)"
                        if args[0].inv[item] < quantity * amount:
                            return f"{args[0].username}, You do not own {quantity * amount} {item}(s)"

                # remove components
                for component in craft_list[craftable]:
                    for item, quantity in component.items():
                        args[0].inv[item] -= quantity * amount

                for item in item_list:
                    if craftable in item[0].keys():
                        if item[1] == 'Card':
                            # add card to card menu
                            if craftable not in args[0].cards:
                                args[0].cards[craftable] = 0
                            args[0].cards[craftable] += amount  # give player crafted item
                            start_update_csv(args[2])
                            return f"{args[0].username} crafted {amount} {craftable}."


                # test if craftable exists
                if craftable not in args[0].inv:
                    args[0].inv[craftable] = 0
                args[0].inv[craftable] += amount  # give player crafted item

                start_update_csv(args[2])
                return f"{args[0].username} crafted {amount} {craftable}."

    craft_display = list(craft_list.items())
    craft_page = 0
    if len(args[3]) > 0:
        try:
            craft_page = int(args[3][0]) - 1  # account for array start = 0
        except Exception as e:
            return e
    min_shown = 0 + (12 * craft_page)
    max_shown = 12 + (12 * craft_page)

    if max_shown > len(craft_list):
        max_shown = len(craft_list)
        min_shown = len(craft_list) - 10

    craft_display_string = f"Crafting List (Page {craft_page + 1}):\n\n"

    for item in craft_display[min_shown:max_shown]:
        craft_display_string += f"{item[0]} : "


        for requirements in item[1]:
            for component, amount in requirements.items():
                if int(amount) > 1:
                    craft_display_string += f"{amount} {component} + "
                else:
                    craft_display_string += f"{component} + "
        craft_display_string = craft_display_string[:-3] + "\n"

    craft_display_string += "      \nType: 'craft (item) (amount)' to craft it:"
    craft_display_string += "\nType: 'craft (number)' to see other pages"
    return craft_display_string
