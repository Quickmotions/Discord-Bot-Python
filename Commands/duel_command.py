from events_manager import start_combat


def duel_c(*args):
    """Starts a one on one pvp battle which can be bet on"""
    if len(args[3]) > 0:
        bet = 0

        if len(args[3]) > 1:
            try:
                bet = int(args[3][1])
            except ValueError as e:
                return f"Incorrect bet value, only use positive numbers and avoid decimals.\n" \
                       f"Try `duel @username (optional: bet amount)`\n{e}"
        for target in args[2]:
            if args[3][0] == f"<@!{target.user_id}>" or args[3][0] == f"<@{target.user_id}>":
                if args[3][0] == f"<@!{args[0].user_id}>" or args[3][0] == f"<@{args[0].user_id}>":
                    return f"You cannot duel yourself.\nTry `Duel (@username) (optional: bet amount)`"
                group = [[args[0].user_id, args[0].username], [target.user_id, target.username]]
                return start_combat(group, args[2], None, 'PVP', args[4])
        return f"Error: Incorrect or missing user specified"
    else:
        return f"Incorrect use of command: Duel.\nTry `Duel (@Username) (Optional: Bet Amount)`"
