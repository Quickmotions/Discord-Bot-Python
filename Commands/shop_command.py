from Commands.update_csv import start_update_csv

shop_list = {
    'Slash': 200,
    'Defend': 320,
    'Charge': 470,
    'Recharge': 600,
    'Punch': 500,
    'Shieldbash': 850,
    'Bash': 620,
    'Slice': 800,
    'Snipe': 1500,
    'Trickshot': 1200,
    'Whirlwind': 2600,
    'Bomb': 1999,
    'Towershield': 4200,
    'Slam': 5500,
    'Incinerate': 4100,
    'Devastate': 2800,
    'Bite': 3600,
    'Venom': 4300,
    'Smash': 3100,
    'Regeneration': 6500,
    'Onepunch': 100000,
}
shop_item_list = {
    'Pickaxe': 300,
    'Fishingrod': 300,
    'Axe': 300,
    'Coal': 20,
    'Crystalium': 125,


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
