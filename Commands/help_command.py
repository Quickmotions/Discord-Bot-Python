def help_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    print(f'Commands are:')
    for each in args[1].command_list:
        print(f'\t-{each}')
