from Commands.update_csv import start_update_csv

craft_list = {
    'IronIngot': [{'Ironore': 2}, {'Coal': 1}],
    'TinIngot': [{'Tinore': 2}, {'Coal': 1}],
    'GoldIngot': [{'Goldore': 2}, {'Coal': 1}],
    'FishIngot': [{'Cod': 10}, {'Tuna': 10}, {'Catfish': 10}, {'Trout': 10}, {'Carp': 10}, {'Mackerel': 10},
                  {'Salmon': 10}],
    'GemIngot': [{'Ruby': 10}, {'Sapphire': 10}, {'Diamond': 10}],
    'CutStone': [{'Stone': 2}],
    'CutLimestone': [{'Limestone': 2}],
    'CutBasalt': [{'Basalt': 2}],
    '': '',
    'FishMeal': [{'Cod': 15}, {'Tuna': 15}, {'Catfish': 15}, {'Trout': 5}],
    'FishSoup': [{'Carp': 10}, {'Mackerel': 10}, {'Salmon': 10}, {'Trout': 5}],
    ' ': '',
    'TinHelmet': [{'TinIngot': 50}],
    'TinChestplate': [{'TinIngot': 80}],
    'TinLeggings': [{'TinIngot': 70}],
    'TinBoots': [{'TinIngot': 40}],
    '  ': '',
    'ThiefHelmet': [{'GoldIngot': 20}, {'Leather': 100}],
    'ThiefChestplate': [{'GoldIngot': 30}, {'Leather': 100}],
    'ThiefLeggings': [{'GoldIngot': 25}, {'Leather': 100}],
    'ThiefBoots': [{'GoldIngot': 15}, {'Leather': 100}],
    '   ': '',
    'WarriorHelmet': [{'IronIngot': 70}, {'Ruby': 20}],
    'WarriorChestplate': [{'IronIngot': 100}, {'Ruby': 30}],
    'WarriorLeggings': [{'IronIngot': 90}, {'Ruby': 25}],
    'WarriorBoots': [{'IronIngot': 60}, {'Ruby': 15}],
    '    ': '',
    'FishHelmet': [{'FishIngot': 20}],
    'FishChestplate': [{'FishIngot': 20}],
    'FishLeggings': [{'FishIngot': 20}],
    'FishBoots': [{'FishIngot': 20}],
    '     ': '',
    'MinerHelmet': [{'GemIngot': 15}],
    'MinerChestplate': [{'GemIngot': 20}],
    'MinerLeggings': [{'GemIngot': 20}],
    'MinerBoots': [{'GemIngot': 20}],
    '      ': '',
    'IronSword': [{'IronIngot': 150}],
    'MagicStaff': [{'GoldIngot': 80}],
    'GemFishingRod': [{'GemIngot': 20}],
    'LuckyStick': [{'GemIngot': 20}],
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

                # test if craftable exists
                if craftable not in args[0].inv:
                    args[0].inv[craftable] = 0
                args[0].inv[craftable] += amount  # give player crafted item

                start_update_csv(args[2])
                return f"{args[0].username} crafted {amount} {craftable}."
    else:
        craft_list_string = "Crafting List:\n          \n"
        for item in craft_list:
            craft_list_string += f"{item} : "
            for component in craft_list[item]:
                if isinstance(component, dict):
                    for multiple_item in component.items():
                        craft_list_string += f"{multiple_item[1]} {multiple_item[0]} + "
                else:
                    craft_list_string += f"{component} + "
            craft_list_string = craft_list_string[:-3] + "\n"

        craft_list_string += "      \nType: 'craft (item) (amount)' to craft it:"
        return craft_list_string
