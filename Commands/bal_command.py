from operator import itemgetter
def bal_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:  # test for arg
        for user in args[2]:

            if str(args[3][0]) == f"<@!{user.user_id}>" or str(args[3][0]) == f"<@{user.user_id}>":
                return f'Bal for {user.username}: £{user.bal}'

            if str(args[3][0]).lower() == "top":
                bal_top = "--Richest users--\n"
                balls = []
                for player in args[2]:
                    balls.append([player.bal, player.username])
                for bal in sorted(balls, key=itemgetter(0), reverse=True)[:6]:
                    bal_top += f"{bal[1]}: £{bal[0]}\n"
                return bal_top

        return f'Bal for {args[0].username}: £{args[0].bal}'

    else:
        return f'Bal for {args[0].username}: £{args[0].bal}'
