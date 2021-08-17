def inv_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    print(f"{args[0].user_id}s Inventory:")
    for item, value in args[0].inv.items():
        if int(value) > 0:
            print(item, ':', value)

