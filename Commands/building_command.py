# data stored in list
# items: land plots, building list, building buffs,
from Commands.update_csv import start_update_csv


building_list = {
    'Shack': [{'OakPlanks': 200}, 'Grants 50 tp per day', 'item', {'TrainingPoint': 50}],
    'LogCabin': [{'PineLog': 500}, 'Grants 🪙480 coins per day', 'money', {'Money': 480}],
    'Armoury': [{'CutStone': 200, 'MaplePlanks': 100}, 'Grants 5 combat skill', 'stats', {'Combat': 5}],
    'MagicTower': [{'CutStone': 100, 'CutBasalt': 100}, 'Grants 5 Magic skill', 'stats', {'Magic': 5}],
    'TrainingRoom': [{'CutStone': 100, 'CutBasalt': 100}, 'Grants 5 Agility skill', 'stats', {'Agility': 5}],

}


def land_c(*args):
    if len(args[3]) > 0:
        if args[3][0] in ["view", "list"]:
            title = f"{args[0].username}s Land"
            if len(args[0].buildings) == 0:
                return f"You own no land. Buy some with land buy."
            land_list = f""
            for land in args[0].buildings:
                land_list += f"{land[0]}\n"
            return title, land_list
        if args[3][0] in ["buy", "purchase", "get", "shop"]:
            title = f"Land Shop"
            if len(args[3]) < 2:
                land_amount_owned = len(args[0].buildings)
                shop_list = f"New Land Plot - 🪙{round(((land_amount_owned * 1.75) + 1) * 4000)}\n"
                shop_list += "-----------\nBuildings:\n-----------\n"
                for building_name, info in building_list.items():
                    price, reward_text, reward_type, reward = info
                    shop_list += f"{building_name} - "
                    for item, amount in price.items():
                        shop_list += f"{amount} {item}, "
                    shop_list = shop_list[:-2] + "\n"
                shop_list += "-----------\nuse: `Land Buy (item)` to buy it.\n" \
                             "use: `Land Info (item)` to see info about that building"
                return title, shop_list
            else:
                if args[3][1].lower() in ["land", "emptyland", "empty"]:
                    price = round(((len(args[0].buildings) * 1.75) + 1) * 4000)
                    if args[0].bal >= price:
                        args[0].bal -= price
                        args[0].buildings.append(["Empty Land"])
                        start_update_csv(args[2])
                        return f"{args[0].username} Purchases Land", f"You Bought 1 empty land for {price}"
                    else:
                        return f"Not enought Money", f"You only own 🪙{args[0].bal} this land costs 🪙{price}"
                for building_name, info in building_list.items():
                    if building_name.lower() == args[3][1].lower():
                        price, reward_text, reward_type, reward = info
                        if "Empty Land" in args[0].buildings:




