from Commands.update_csv import start_update_csv

shop_list = {
    'slash': 200,
    'defend': 320,
    'charge': 470,
    'recharge': 600,
    'punch': 500,
    'shieldbash': 850,
    'bash': 620,
    'slice': 800,
    'snipe': 1500,
    'trickshot': 1200,
    'whirlwind': 2600,
    'bomb': 1999,
    'towershield': 4200,
    'slam': 5500,
    'incinerate': 4100,
    'devastate': 2800,
    'bite': 3600,
    'venom': 4300,
    'smash': 3100,
    'regeneration': 6500,
    'Wrath': 9500,
    'FrostArrow': 7340,
    'Corruption': 14000,
    'onepunch': 100000,
}
shop_item_list = {
    'pickaxe': 300,
    'fishingrod': 300,
    'axe': 300,
    'coal': 20,

}


def shop_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        if len(args[3]) > 1:
            if args[3][0] == "buy":
                # card shop
                for item in shop_list:
                    if item == str(args[3][1]):
                        amount = 1
                        if len(args[3]) > 2:
                            amount = int(args[3][2])
                        if args[0].bal >= shop_list[item] * amount:
                            args[0].bal -= shop_list[item] * amount
                            if item.title() not in args[0].cards:  # add item to card list if it doesnt exist
                                args[0].cards[item.title()] = 0
                            args[0].cards[item.title()] += amount
                            start_update_csv(args[2])
                            return f"Bought {amount} {item} for £{shop_list[item] * amount}"
                        else:
                            return f"You dont own enough money:\nItem - {amount} {item} costs £{shop_list[item] * amount}"
                # item shop
                for item in shop_item_list:
                    if item == str(args[3][1]):
                        amount = 1
                        if len(args[3]) > 2:
                            amount = int(args[3][2])
                        if args[0].bal >= shop_item_list[item] * amount:
                            args[0].bal -= shop_item_list[item] * amount
                            if item.title() not in args[0].inv:  # add item to card list if it doesnt exist
                                args[0].inv[item.title()] = 0
                            args[0].inv[item.title()] += amount
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
