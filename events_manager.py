from Commands.update_csv import start_update_csv
from datetime import datetime
import random
import ast
from Mobs.mob_loot import award_hunt_loot
from Commands.update_skills import give_xp


def get_events():
    events = []
    f = open("events.csv", "r")
    for event in f.readlines():
        event.strip()
        events.append(ast.literal_eval(event))
    return events


def draw_card_deck(user, draw_amount=3):
    user_deck = user.cards
    deck = []
    for card in user_deck:  # get all cards in deck
        for _ in range(user_deck[card]):  # add card multiple times for how many user owns
            deck.append(card)

    draw = []

    for _ in range(draw_amount):  # draw an amount of cards
        card_drawn = random.choice(deck)
        deck.remove(card_drawn)
        draw.append(card_drawn)

    return draw


def start_combat(user, users, mob, battle_type):
    user_party = []
    for member in user.party:
        if member[2] == 'member':
            user_party.append(member)

    events = get_events()
    for event in events:
        for member in event[2]:
            if str(member[0]) == user.user_id:
                return f"You already have an active combat:\nComplete the event first."

    event_data = [0, battle_type, user_party]
    user_data = []
    for member in user_party:
        for user in users:
            if user.user_id == member[0]:
                # set up health
                health_base = user.skills['Health'] + user.equipment_stats['Health']
                magic_base = user.skills['Magic'] + user.equipment_stats['Magic']
                critical_base = user.skills['Critical'] + user.equipment_stats['Critical']

                max_hp = round(100 * ((((6 * health_base) - (2 * magic_base) - (1 * critical_base)) / 100) + 1))
                if max_hp < 1:
                    max_hp = 1
                hp = max_hp

                user_data.append([hp, max_hp, 0, draw_card_deck(user)])

    event_data.append(user_data)
    event_data.append([mob[0], mob[1], mob[2], mob[2], mob[3], mob[4]])

    # info about EVENT_DATA: ----------------------------
    # turn, battle_type, party, user_data, mob_data
    # ---------------------------------------------------
    # party = [user_id, username, 'member/invite'] * party
    # user_data = [hp, maxhp, shield, draw] * party
    # mob_data = [dificulty, name. hp, maxhp, dmg, coins]
    # ---------------------------------------------------

    f = open("events.csv", 'a')
    f.write(f'{event_data}\n')
    f.close()

    gui = create_battle_gui(event_data, start=True)
    return gui


def create_battle_gui(event_data, start=False):
    turn, battle_type, party, user_data, mob = event_data
    gui = ["multiple"]
    players_gui = ""
    if start:
        for pos in range(len(party)):
            players_gui += f"{party[pos][1]}:\n💗: {user_data[pos][0]}/{user_data[pos][1]}\n🛡️: {user_data[pos][2]}\n"


    players_gui += f"{mob[1]}:\n💗: {mob[2]}/{mob[3]}\n🗡️: {mob[4]}"
    gui.append(players_gui)
    gui.append(f"{party[turn][1]}s Turn:\n{user_data[turn][3]}")

    return gui




def check_event_response(*args):
    # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list 4 = events 5 = input message
    events = get_events()









    if args[5] == "1" or args[5] == "2" or args[5] == "3" or args[5] == "4":  # test if user input is valid for fight
        for event in args[4]:
            if event.user_id == args[0].user_id:
                if event.active == "Active=Yes":
                    # player turn
                    draw = list(event.draw)
                    if args[5] == "1":
                        choice = 0
                    if args[5] == "2":
                        choice = 1
                    if args[5] == "3":
                        choice = 2
                    if args[5] == "4":
                        if len(draw) > 3:
                            choice = 3
                        else:
                            return "Only 3 cards were drawn."

                    from Commands.card_command import use_card

                    info = use_card(draw[choice], args[0], event)

                    # healing
                    healing = info[3]
                    if event.hp + healing > event.max_hp:
                        event.hp = event.max_hp
                    else:
                        event.hp += healing

                    # can player draw extra card
                    if info[2]:
                        new_draw = draw_card_deck(args[0], 4)
                    else:
                        new_draw = draw_card_deck(args[0])

                    # dodge
                    dodge_chance = info[4]
                    # enemy turn

                    if event.mob_hp <= 0:  # is mob dead?
                        event.active = "Active=No"
                        start_update_events(args[4])


                        coins_gained = float(event.mob_coins) / 100
                        coins_gained = round(coins_gained * random.randint(90, 110), 2)
                        huntp_gain = round(event.mob_coins / random.randint(4, 7))

                        args[0].bal += coins_gained
                        if 'HuntPoint' not in args[0].inv:
                            args[0].inv['HuntPoint'] = 0
                        args[0].inv['HuntPoint'] += huntp_gain


                        loot_gained = award_hunt_loot(event.difficulty, args[0], args[2])
                        loot_message = ""
                        if loot_gained is not None:
                            for loot in loot_gained:
                                loot_message += f"{loot[1]} {loot[0]}\n"

                        xp_gain = round((coins_gained / 3) * (1 + 0.1 * (random.randint(-4, 4))))
                        give_xp(xp_gain, "Player", args[0], args[2])

                        start_update_csv(args[2])
                        start_update_events(args[4])
                        return f"You defeated {event.mob_name}:\n" \
                               f"You looted:\n" \
                               f"{coins_gained} money\n" \
                               f"{xp_gain} Player XP\n" \
                               f"{huntp_gain} HuntPoint\n" \
                               f"{loot_message}"

                    piercing_attack = False
                    if random.randint(1, 12) == 1:
                        piercing_attack = True

                    dodged = True
                    if random.randint(1, 100) > dodge_chance:
                        dodged = False
                        enemy_damage = random.randint(event.mob_dmg - 1, event.mob_dmg + 1)
                        if not piercing_attack:
                            for _ in range(enemy_damage):
                                if event.shield > 0:
                                    event.shield -= 1
                                else:
                                    event.hp -= 1
                        if piercing_attack:
                            event.hp -= enemy_damage


                    # is player dead
                    if event.hp <= 0:
                        event.active = "Active=No"
                        start_update_events(args[4])
                        coins_lost = round(event.mob_coins * 3, 2)
                        if args[0].bal < coins_lost:
                            coins_lost = args[0].bal
                        args[0].bal -= coins_lost
                        start_update_csv(args[2])
                        start_update_events(args[4])
                        return f"You were defeated by {event.mob_name}:\n They stole £{coins_lost} from you"


                    # mob hp left percent
                    mob_hp_percent = round((100 / event.mob_max_hp) * event.mob_hp)

                    event.draw = new_draw
                    start_update_events(args[4])

                    draw_menu = "Your Cards:\n"
                    num = 1
                    for card in new_draw:
                        draw_menu += f"{num} = {card}\n"
                        num += 1
                    if dodged:
                        return ["multiple", f"{args[0].username}:\n❤️: {event.hp} - Dodged + {healing}\n🛡️:"
                                            f" {event.shield} + {info[1]}\n🗡️: {info[0]}\n{event.mob_name}:\n"
                                            f"❤️: {event.mob_hp} ({mob_hp_percent}%) - {info[0]}\n🗡️: Dodged({dodge_chance}%)",
                                f"{draw_menu}"]

                    if not piercing_attack:
                        return ["multiple", f"{args[0].username}:\n❤️: {event.hp} - {enemy_damage} + {healing}\n🛡️:"
                                        f" {event.shield} + {info[1]}\n🗡️: {info[0]}\n{event.mob_name}:\n"
                                        f"❤️: {event.mob_hp} ({mob_hp_percent}%) - {info[0]}\n🗡️: {enemy_damage}",
                                        f"{draw_menu}"]
                    else:
                        return ["multiple", f"{args[0].username}:\n❤️: {event.hp} - 🪡{enemy_damage} + {healing}\n🛡️:"
                                            f" {event.shield} + {info[1]}\n🗡️: {info[0]}\n{event.mob_name}:\n"
                                            f"❤️: {event.mob_hp} ({mob_hp_percent}%) - {info[0]}\n🗡️: {enemy_damage}",
                                f"{draw_menu}"]

    return None
