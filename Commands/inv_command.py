def inv_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    response = f"{args[0].username}s Inventory:\n--------------------"

    for item, value in args[0].inv.items():
        if int(value) > 0:
            response += f"\n{item} : {value}"

    return response
