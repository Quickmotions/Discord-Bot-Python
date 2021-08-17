def bal_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:  # test for arg
        for user in args[2]:
            if str(args[3][0]) == f"<@!{user.user_id}>":
                return f'Bal for {user.username}: £{user.bal}'
        return f'Bal for {args[0].username}: £{args[0].bal}'
    else:
        return f'Bal for {args[0].username}: £{args[0].bal}'
