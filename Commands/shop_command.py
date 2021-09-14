from Commands.update_csv import start_update_csv

shop_list = {
    'Slash': 600,
    'Defend': 700,
    'Charge': 1200,
    'Recharge': 1200,
    'Punch': 2200,
    'Shieldbash': 3500,
    'Bash': 2100,
    'Slice': 2400,
    'Snipe': 4300,
    'Trickshot': 3200,
    'Whirlwind': 5200,
    'Bomb': 2000,
    'Towershield': 6200,
    'Slam': 10500,
    'Incinerate': 5100,
    'Devastate': 6000,
    'Bite': 7800,
    'FirstAid': 9680,
    'Venom': 8900,
    'Smash': 7900,
    'MultiShot': 13400,
    'QuickStab': 7800,
    'Restoration': 9000,
    'Regeneration': 12200,
    'Guard': 75000,
    'Onepunch': 80000,
}
shop_item_list = {
    'Pickaxe': 1500,
    'Fishingrod': 1500,
    'Axe': 1500,
    'Coal': 20,
    'Crystalium': 125,
    'Catalyst': 945,


}


def shop_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        if len(args[3]) > 1:
            if args[3][0] == "buy":
                # card shop
                for item in shop_list:
                    if item.lower() == args[3][1].lower():
                        amount = 1
                        if len(args[3]) > 2:
                            amount = int(args[3][2])
                        if args[0].bal >= shop_list[item] * amount:
                            args[0].bal -= shop_list[item] * amount
                            if item not in args[0].cards:  # add item to card list if it doesnt exist
                                args[0].cards[item] = 0
                            args[0].cards[item] += amount
                            start_update_csv(args[2])
                            return f"Bought {amount} {item} for £{shop_list[item] * amount}"
                        else:
                            return f"You dont own enough money:\nItem - {amount} {item} costs £{shop_list[item] * amount}"
                # item shop
                for item in shop_item_list:
                    if item.lower() == args[3][1].lower():
                        amount = 1
                        if len(args[3]) > 2:
                            amount = int(args[3][2])
                        if args[0].bal >= shop_item_list[item] * amount:
                            args[0].bal -= shop_item_list[item] * amount
                            if item not in args[0].inv:  # add item to card list if it doesnt exist
                                args[0].inv[item] = 0
                            args[0].inv[item] += amount
                            start_update_csv(args[2])
                            return f"Bought {amount} {item} for £{shop_item_list[item] * amount}"
                        else:
                            return f"You dont own enough money:\nItem - {amount} {item} costs £{shop_list[item] * amount}"
                return "Item not in found in shop"
            else:
                return "To buy an item from the shop:\nUse 'shop buy (item) (amount)'"
        else:
            return "To buy an item from the shop:\nUse 'shop buy (item) (amount)'"

    else:
        shop_menu = "Shop Menu:\n--Cards--\n"
        for item in shop_list:
            shop_menu += f"{item.title()} : £{shop_list[item]}\n"
        shop_menu_item = "Shop Menu:\n--Items--\n"
        for item in shop_item_list:
            shop_menu_item += f"{item.title()} : £{shop_item_list[item]}\n"
        shop_menu_item += "Type: 'shop buy (item) (amount)' to buy it:"
        return ["multiple", shop_menu, shop_menu_item]
