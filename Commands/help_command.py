def help_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    response = "Commands are: "
    for each in args[1].command_list:
        response += f'\n-{each}'
    return response
