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
    'regeneration': 7500,
    'onepunch': 100000
}


def shop_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        if len(args[3]) > 1:
            if args[3][0] == "buy":
                for item in shop_list:
                    print(item)
                    if item == str(args[3][1]):
                        if args[0].bal >= shop_list[item]:
                            args[0].bal -= shop_list[item]
                            if item.title() not in args[0].cards:  # add item to card list if it doesnt exist
                                args[0].cards[item.title()] = 0
                            args[0].cards[item.title()] += 1
                            return f"Bought 1 {item}"
                        else:
                            return f"You dont own enough money:\nItem - {item} costs £{shop_list[item]}"
                return "Item not in found in shop"
            else:
                return "To buy an item from the shop:\nUse 'shop buy (item)'"
        else:
            return "To buy an item from the shop:\nUse 'shop buy (item)'"

    else:
        shop_menu = "Shop Menu:\n---------------\n"
        for item in shop_list:
            shop_menu += f"{item.title()} - £{shop_list[item]}\n"

        return shop_menu
