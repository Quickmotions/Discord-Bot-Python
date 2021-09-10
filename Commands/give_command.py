from Commands.update_csv import start_update_csv
from Commands.item_command import item_list

def give_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 1:  # test for arg
        for user in args[2]:
            if f"<@!{user.user_id}>" == str(args[3][0]) or f"<@{user.user_id}>" == str(args[3][0]):  # test @
                amount_to_send = int(args[3][1])  # set amount
                # admin send
                if len(args[3]) > 3:
                    if args[3][3] == "admin" and args[0].user_id == "482271768451612683":
                        for item, slot, stats in item_list:
                            for item_name, desc in item.items():
                                if item_name.lower() == args[3][2]:
                                    if len(args[3]) > 3:
                                        if item_name not in user.inv:
                                            user.inv[item_name] = 0
                                        user.inv[item_name] += amount_to_send
                                        start_update_csv(args[2])
                                        return f"Admin gave {amount_to_send} {item_name} to {user.username}"
                # normal send
                if amount_to_send <= 0:
                    return f"Cannot send {amount_to_send}:\nTry an amount above 0 that's not a decimal."

                # send item
                if len(args[3]) > 2:
                    item_to_send = str(args[3][2]).lower()
                    for name, amount in args[0].inv.items():
                        if item_to_send == str(name.lower()):
                            if amount_to_send > amount:
                                return f"You do not own {amount_to_send} {name}"
                            if name not in user.inv:
                                user.inv[name] = 0
                            user.inv[name] += amount_to_send
                            args[0].inv[name] -= amount_to_send

                            start_update_csv(args[2])
                            return f"{args[0].username} sent {amount_to_send} {name} to {user.username}"
                    return f"Item {item_to_send} not found in inventory."

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

