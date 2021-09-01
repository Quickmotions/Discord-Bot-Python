import random


def rob_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        rob_victim = str(args[3][0])
        for victim in args[2]:
            if rob_victim == f"<@!{victim.user_id}>" or rob_victim == f"<@{victim.user_id}>":  # test if target exists
                if rob_victim == f"<@!{args[0].user_id}>" or rob_victim == f"<@{args[0].user_id}>":  # test if self
                    return "Cant rob yourself:\nTry 'rob @username'"
                else:
                    if victim.bal >= 100.0:  # target must have £100 or more
                        # largest amount to steal
                        user_steal = args[0].skills['Stealing'][0] + args[0].equipment_stats['Stealing']
                        victim_defense = victim.skills['Defense'][0] + victim.equipment_stats['Defense']
                        base_steal = 0.3

                        steal_multiplier = float(((user_steal - victim_defense) / 100) + 1)

                        # find chance to steal and test chance
                        chance = 30
                        if user_steal < victim_defense:
                            chance = 10
                        if user_steal > victim_defense:
                            chance = 60
                        if user_steal - victim_defense >= 2:
                            chance = 60 + random.randint(5, 15)

                        if random.randint(1, 100) > chance:
                            # steal failed
                            return f"Robbed {victim.username}:\nYour Stealing: {user_steal}" \
                                   f", Their Defense: {victim_defense}\nYou Failed\nYou had a {chance}% to rob them."

                        amount_to_steal = (victim.bal * base_steal) * steal_multiplier

                        # stop over stealing max
                        if amount_to_steal > victim.bal:
                            amount_to_steal = victim.bal

                        # change money over
                        victim.bal -= amount_to_steal
                        args[0].bal += amount_to_steal

                        # round both users balance
                        args[0].bal = round(args[0].bal, 2)
                        victim.bal = round(victim.bal, 2)

                        from Commands.update_csv import start_update_csv
                        start_update_csv(args[2])

                        return f"Robbed {victim.username}:\nYour Stealing: {args[0].skills['Stealing'][0]}" \
                               f", Their Defense: {victim.skills['Defense'][0]}\nYou Got £{amount_to_steal} " \
                               f"from your victim\nYou had a {chance}% to rob them."
                    else:
                        return "Victim doesnt even have enough money:\nTry when they have more than £100"
        return "Invalid victim:\nTry 'rob @username'"
    else:
        return "No victim Specified:\nTry 'rob @username'"
