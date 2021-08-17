def bal_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:  # test for arg
        for user in args[2]:
            if str(args[3][0]) == str(user.user_id):
                print(f'Bal for {user.user_id}: £{user.bal}') # show specific users bal
                return
        print(f'Bal for {args[0].user_id}: £{args[0].bal}')
    else:
        print(f'Bal for {args[0].user_id}: £{args[0].bal}')
        return
