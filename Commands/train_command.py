def train_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        if args[0].inv['Training Point'] > 0:
            pass
        else:
            return 'Must have at least 1 training point'
    else:
        return "Incorrect use of train command\nuse train (skill) (optional: amount of points to spend)"