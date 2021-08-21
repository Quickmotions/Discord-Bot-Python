from Commands.update_csv import start_update_csv


def gamble_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        # adds luck skill if the user has never had any
        if 'Luck' not in args[0].skills:
            args[0].skills['Luck'] = [0, 0, 100]
        amount_to_gamble = round(float(args[3][0]), 2)
        user_luck = int(args[0].skills['Luck'][0])
        luck_multiplier = round(user_luck * 0.3)
        user_bal = args[0].bal
        if amount_to_gamble > user_bal:
            return f"You don't own that much:\n Try 'gamble {user_bal}' to gamble all your money"
        if amount_to_gamble < 0:
            return f"Cant gamble less than £0"
        chance = 20 + luck_multiplier

        import random

        if random.randint(1, 100) <= chance:
            winnings = round((amount_to_gamble * 0.6), 2)
            args[0].bal += winnings
            start_update_csv(args[2])
            return f"You won:\n£{winnings} was added to your balance"
        else:
            args[0].bal -= amount_to_gamble
            start_update_csv(args[2])
            return f"You Lost:\n£{amount_to_gamble} has been removed from your balance"

    else:
        return f"Invalid amount:\nplease specify amount to gamble"

