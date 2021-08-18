def give_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    return "Give is Currently Disabled"
    # DEBUG ^
    if len(args[3]) > 1:  # test for arg
        for user in args[2]:
            if f"<@!{user.user_id}>" == str(args[3][0]) or f"<@{user.user_id}>" == str(args[3][0]):
                # tests for user with same id as submitted arg
                try:
                    arg_amount = float(args[3][1])  # gets submitted arg for val
                    user.bal += arg_amount
                    return f"Gave {user.username}: {arg_amount} coins!"
                except:
                    return "Invalid amount"

        from Commands.update_csv import start_update_csv
        start_update_csv(args[2])
    else:
        return "Missing args:\nGive (user) (+-)(val)"

