from Commands.update_csv import start_update_csv

def give_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 1:  # test for arg
        for user in args[2]:
            if f"<@!{user.user_id}>" == str(args[3][0]) or f"<@{user.user_id}>" == str(args[3][0]):  # test @

                amount_to_send = int(args[3][1])  # set amount
                if amount_to_send <= 0:
                    return f"Cannot send {amount_to_send}:\nTry an amount above 0 that's not a decimal."
                # send item
                if len(args[3]) > 2:
                    item_to_send = str(args[3][2]).lower()
                    for name, amount in args[0].inv.items():
                        if item_to_send == str(name.lower()):
                            if len(args[3]) > 3:

                                # admin send no cost
                                if args[3][3] == "admin" and args[0].user_id == "482271768451612683":
                                    if name not in user.inv:
                                        user.inv[name] = 0
                                    user.inv[name] += amount_to_send
                                    start_update_csv(args[2])
                                    return f"{args[0].username} sent {amount_to_send} {name} to {user.username}"

                            if amount_to_send > amount:
                                return f"You do not own {amount_to_send} {name}"
                            if name not in user.inv:
                                user.inv[name] = 0
                            user.inv[name] += amount_to_send
                            args[0].inv[name] -= amount_to_send

                            start_update_csv(args[2])
                            return f"{args[0].username} sent {amount_to_send} {name} to {user.username}"
                else:
                    # send money
                    if amount_to_send > args[0].bal:
                        return f"You don't own £{amount_to_send} to send to {user.username}"

                    args[0].bal -= amount_to_send
                    user.bal += amount_to_send
                    start_update_csv(args[2])
                    return f"{args[0].username} sent £{amount_to_send} to {user.username}"
        return "Missing User:\ntry 'give (@user) (amount £)' or 'give (@user) (amount) (itemname):" \
               "\nGive doesnt work with decimals'"
    else:
        return "Missing args:\ntry 'give (@user) (amount £)' or 'give (@user) (amount) (itemname)':" \
               "\nGive doesnt work with decimals"

