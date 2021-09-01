from Commands.update_csv import start_update_csv


def removal_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if 'RemovalSigil' in args[0].inv:
        if args[0].inv['RemovalSigil'] > 0:
            if len(args[3]) > 0:
                card_chosen = str(args[3][0]).lower()
                for card in args[0].cards:
                    if card_chosen == card.lower():
                        args[0].cards[card] -= 1
                        args[0].inv['RemovalSigil'] -= 1
                        start_update_csv(args[2])
                        return f"{args[0].username}: removed {card} from your deck for 1 RemovalSigil."
                return f"You do not own the card {card_chosen}\nTry 'removal (card name)'"
            else:
                return "Incorrect use of command\nTry 'removal (card name)'"

        else:
            return "You do not own any removal sigils"
    else:
        return "You do not own any removal sigils"