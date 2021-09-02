import random


def steal_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    user_steal = args[0].skills['Stealing'] + args[0].equipment_stats['Stealing']
    coins = random.randint(1, 10)
    steal_multiplier = float((user_steal / 100) + 1)

    amount_to_steal = round(coins * steal_multiplier, 2)
    if random.randint(1, 100) + user_steal >= 50:
        args[0].bal += amount_to_steal
        return f"Managed to steal: \nYou got £{amount_to_steal} from an unsuspecting victim."

    else:
        if args[0].bal >= 15:
            amount_to_lose = round(random.randint(1, 14), 2)
            args[0].bal -= amount_to_lose
            return f"Failed to steal: \nYou got fined £{amount_to_lose}."



