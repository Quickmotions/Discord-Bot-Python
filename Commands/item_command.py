item_list = {
    'pickaxe': 'Used to mine rocks',
    'fishingrod': 'Used to fish',
    'removalsigil': 'Can be consumed to remove one card from your deck'
}


def item_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        for item in item_list:
            if args[3][0] == item.lower():
                return f"Info for {args[3][0].title()}:\n{item_list[args[3][0]]}"
    else:
        return f"Incorrect use of item:\ntry 'item (item-name)'"
