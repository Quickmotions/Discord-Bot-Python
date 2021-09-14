from Commands.update_csv import start_update_csv


def loadout_c(*args):
    if len(args[3]) > 0:
        if args[3][0] in ["buy", "purchase", "add"]:
            if args[0].bal >= 100000:
                args[0].bal -= 100000
                args[0].loadout.append({'Slash': 3, 'Defend': 1, 'Charge': 1})
                start_update_csv(args[2])
                return f"Bought 1 loadout for 🪙100000. You now have {len(args[0].loadout)} loadouts."
            else:
                return "You do not own enough 🪙\nEach Loadout costs 🪙100000"

        else:
            if args[3][0].isnumeric():
                val = int(args[3][0]) - 1
                if val + 1 <= len(args[0].loadout):
                    args[0].cards = args[0].loadout[val]
                    start_update_csv(args[2])
                    return f"Replaced your current loadout with loadout {val + 1}."
                else:
                    return f"You do not own loadout number {val + 1}\nBuy more loadouts with `loadout buy` for 🪙100000"

    loadout_lists = ""
    count = 1
    for loadout in args[0].loadout:
        loadout_lists += f"Loadout {count}:\n"
        for card, amount in loadout.items():
            loadout_lists += f"{amount} {card}, "
        loadout_lists = loadout_lists[:-2] + "\n\n"
        count += 1

    loadout_lists += f"Buy more loadouts with `loadout buy` for 🪙100000\n" \
                     f"Or `loadout (number)` to equip that loadout"
    return loadout_lists
