from Commands.update_csv import start_update_csv
from datetime import datetime
import random
import ast
from Commands.item_command import award_hunt_loot
from Commands.update_skills import give_xp


# clear events at start up
f = open("events.csv", 'w').close()


# def get_events():
#     """returns list of on going events """
#     events = []
#     f = open("events.csv", "r")
#     for event in f.readlines():
#         event.strip()
#         if len(event) > 5:
#             events.append(ast.literal_eval(event))  # turns the events line into a list of usable combat data
#     return events


def draw_card_deck(user_id, users, draw_amount=3):
    """sorts users deck into a list and picks returns a random pick from them"""
    # draws a new hand for a specified user
    for user in users:
        if user.user_id == user_id:
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


def start_combat(user, users, mob, battle_type, events):
    """Begins a combat event with data send from hunt command"""
    user_party = []
    for member in user.party:
        if member[2] == 'member':
            user_party.append(member)

    for event in events:
        for member in event[2]:
            for user_id, username, membership in user_party:
                if user_id == str(member[0]):
                    if len(event[2]) == 1 and len(user_party) > 1:
                        events = update_events_csv(event, events, 'delete')
                    elif len(event[2]) > 1 and len(user_party) == 1:
                        events = update_events_csv(event, events, 'delete')
                    else:
                        return f"You need to complete your previous event first"

    event_data = [0, battle_type, user_party]
    user_data = []

    for member in user_party:
        for player in users:
            if str(player.user_id) == member[0]:
                # set up health and dodge
                combat_base = player.skills['Combat'] + player.equipment_stats['Combat']
                defense_base = player.skills['Defense'] + player.equipment_stats['Defense']
                agility_base = player.skills['Agility'] + player.equipment_stats['Agility']
                healing_base = player.skills['Healing'] + player.equipment_stats['Healing']
                health_base = player.skills['Health'] + player.equipment_stats['Health']
                dodge_base = player.skills['Dodge'] + player.equipment_stats['Dodge']

                dodge = ((0.5 * dodge_base) + (0.2 * agility_base) - (0.25 * defense_base))
                max_hp = round(100 * ((((6 * health_base) + (4 * combat_base) + (2 * defense_base) + (3 * healing_base)) / 100) + 1))

                if max_hp < 1:
                    max_hp = 1
                hp = max_hp
                if dodge < 0:
                    dodge = 0

                user_data.append([hp, max_hp, 0, draw_card_deck(user_party[0][0], users), 0, dodge, 0])
    event_data.append(user_data)

    mob_max = round(int(mob[2]) * (1 + (0.6 * (len(user_party) - 1))))
    mob_dmg = round(int(mob[3]) * (1 + (0.2 * (len(user_party) - 1))))
    event_data.append([mob[0], mob[1], mob_max, mob_max, mob_dmg, mob[4]])

    # info about EVENT_DATA: ----------------------------
    # turn, battle_type, party, user_data, mob_data
    # ---------------------------------------------------
    # party = [user_id, username, 'member/invite'] * party
    # user_data = [hp, maxhp, shield, draw, dodge, reg_dodge, cool_down] * party
    # mob_data = [difficulty, name, hp, maxhp, dmg, coins]
    # ---------------------------------------------------

    events = update_events_csv(event_data, events, 'append')

    gui = create_battle_gui(event_data, True)
    return [gui, events]


def create_draw_gui(draw):
    """displays the users hand which they draw"""
    count = 1
    gui = ""
    for card in draw:
        gui += f"{count} - {card}\n"
        count += 1
    return gui


def create_battle_gui(event_data, start, info=[], extra="None"):
    """displays the whole battle view with all info after each turn"""
    turn, battle_type, party, user_data, mob = event_data
    mob_hp_percent = round((100 / int(mob[3])) * int(mob[2]))

    if len(info) > 0:
        damage_dealt, self_damage, shield_gained, extra_draw, heal_gained, extra_draw, dodge, mob_damage, cool_down, mob_attacks, crit = info
        if extra == "dodged":
            mob_damage = f"💨Dodged ({dodge}%)"
        elif extra == "pierce":
            mob_damage = "🪡" + str(mob_damage)
        user_data[turn][4] = dodge

    most_missing = 0
    for pos in range(len(party)):
        missing_current = int(user_data[pos][1]) - int(user_data[pos][0])
        missing_most = int(user_data[most_missing][1]) - int(user_data[most_missing][0])
        if missing_current > missing_most:
            most_missing = pos

    most_hp = 0
    biggest_hp_amount = 0
    for pos in range(len(party)):
        if int(user_data[pos][1]) > biggest_hp_amount and int(user_data[pos][0]) > 0:
            most_hp = pos
            biggest_hp_amount = user_data[pos][1]

    last_turn = turn - 1
    if last_turn < 0:
        last_turn = len(party) - 1

    gui = ["multiple"]
    players_gui = ""

    if start:
        for pos in range(len(party)):
            players_gui += f"{party[pos][1]}:\n" \
                           f"💗 {user_data[pos][0]}/{user_data[pos][1]}\n" \
                           f"🛡️ {user_data[pos][2]}\n"
    else:
        for pos in range(len(party)):
            player_hp_percent = round((100 / user_data[pos][1]) * user_data[pos][0])
            players_gui += f"{party[pos][1]}:\n"
            if pos == most_missing and int(heal_gained) > 0:
                players_gui += f"💗 {user_data[pos][0]}/{user_data[pos][1]} ({player_hp_percent}%) + 💕{heal_gained}"
            else:
                players_gui += f"💗 {user_data[pos][0]}/{user_data[pos][1]} ({player_hp_percent}%)"
            if pos == most_hp:
                if extra == "dodged":
                    players_gui += f" - 🎯{mob_damage}\n"
                elif extra == "pierce":
                    players_gui += f" - 🎯{mob_damage}\n"
                elif int(mob_damage) > 0:
                    players_gui += f" - 🎯{mob_damage}\n"
                else:
                    players_gui += f"\n"
            if pos == last_turn and int(shield_gained) > 0:
                players_gui += f"🛡️ {user_data[pos][2]} + 🛡️{shield_gained}\n"
            else:
                players_gui += f"🛡️ {user_data[pos][2]}\n"
            if pos == last_turn:
                if crit:
                    players_gui += f"💢 {damage_dealt}\n"  # crit emoji
                else:
                    players_gui += f"🗡️ {damage_dealt}\n"  # dagger emoji


    if start:
        players_gui += f"{mob[1]}:\n" \
                       f"💗 {mob[2]}/{mob[3]}\n" \
                       f"🗡️ {mob[4]}"
    else:
        players_gui += f"{mob[1]}:\n"
        if int(damage_dealt) > 0:
            if crit:
                players_gui += f"💗 {mob[2]}/{mob[3]} ({mob_hp_percent}%) - 💢{damage_dealt}\n"
            else:
                players_gui += f"💗 {mob[2]}/{mob[3]} ({mob_hp_percent}%) - 📌{damage_dealt}\n"
        else:
            players_gui += f"💗 {mob[2]}/{mob[3]} ({mob_hp_percent}%)\n"
        players_gui += f"🗡️ {mob_damage}"
        if mob_attacks > 1:
            players_gui += f" ({mob_attacks}x)"

    gui.append(players_gui)
    gui.append(f"{party[turn][1]}s Turn:\n{create_draw_gui(user_data[turn][3])}")
    return gui


def check_event_response(*args):
    """checks users inputs to see if they are in a combat"""
    # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list 4 = events 5 = input message
    if args[4] == "1" or args[4] == "2" or args[4] == "3" or args[4] == "4":
        events = args[5]
        for event in events:
            for member in event[2]:
                if str(member[0]) == args[0].user_id:
                    turn, battle_type, party, user_data, mob_data = event
                    return battle_turn(turn, battle_type, party, user_data, mob_data, args[0], args[2], args[4], events)


def update_events_csv(event_updated, events, update_type):
    """updates the events csv with combat updates after each turn"""
    new_events = []

    # if the party list is empty due to players leaving party mid combat delete the event
    active_events = []
    for event in events:
        if len(event[2]) > 0:
            active_events.append(event)

    events = active_events

    if update_type == 'append':
        # f = open("events.csv", 'a')
        # f.write(f'{event_updated}\n')
        # f.close()
        # return
        new_events.append(event_updated)

    elif update_type == 'delete':
        for position in range(len(events)):
            if str(events[position][2][0]) == str(event_updated[2][0]):
                pass
            else:
                new_events.append(events[position])

    elif update_type == 'update':
        for position in range(len(events)):
            if str(events[position][2][0]) == str(event_updated[2][0]):
                new_events.append(event_updated)
            else:
                new_events.append(events[position])

    else:
        print('ERROR: MISSING OR INCORRECT UPDATE TYPE FOR UPDATE_EVENTS_CSV <----------------------------------------')
        return
    # f = open("events.csv", 'w')
    # for event in new_events:
    #     f.write(f"{event}\n")
    # f.close()
    return new_events


def battle_turn(turn, battle_type, party, user_data, mob_data, user, users, response, events):
    """begins the users, performs the users actions and begins next turn and waits for next users input"""
    if party[turn][0] == user.user_id:
        draw = list(user_data[turn][3])
        if response == "1":
            choice = 0
        if response == "2":
            choice = 1
        if response == "3":
            choice = 2
        if response == "4":
            if len(draw) > 3:
                choice = 3
            else:
                return "Only 3 cards were drawn."

        # player turn
        from Commands.card_command import use_card

        damage_dealt, self_damage, shield_gained, extra_draw, heal_gained, extra_draw, dodge_bonus, cool_down, crit \
            = use_card(draw[choice], user, mob_data)


        user_data[turn][6] += cool_down

        mob_data[2] -= damage_dealt
        user_data[turn][0] -= self_damage
        user_data[turn][2] += shield_gained

        dodge = round(user_data[turn][5] + dodge_bonus)
        user_data[turn][4] = user_data[turn][5] + dodge_bonus
        if user_data[turn][4] < 0:
            user_data[turn][4] = 0
        if user_data[turn][4] > 90:
            user_data[turn][4] = 90

        # healing
        if heal_gained > 0:
            most_missing = turn
            for pos in range(len(party)):
                missing_current = int(user_data[pos][1]) - int(user_data[pos][0])
                missing_most = int(user_data[most_missing][1]) - int(user_data[most_missing][0])
                if missing_current > missing_most:
                    most_missing = pos

            if user_data[most_missing][0] + heal_gained > user_data[most_missing][1]:
                user_data[most_missing][0] = user_data[most_missing][1]
            else:
                user_data[most_missing][0] += heal_gained




        # enemy turn

        if int(mob_data[2]) <= 0:  # is mob dead?

            coins_gained = int(mob_data[5]) / 100
            coins_gained = round(coins_gained * random.randint(90, 110), 2)
            huntP_gain = round(int(mob_data[5]) / random.randint(2, 5))
            xp_gain = round((coins_gained / 3) * (1 + 0.1 * (random.randint(-4, 4))))

            for user in users:
                for player in party:
                    if user.user_id == player[0]:
                        user.bal += coins_gained
                        if 'HuntPoint' not in user.inv:
                            user.inv['HuntPoint'] = 0
                        user.inv['HuntPoint'] += huntP_gain
                        give_xp(xp_gain, "Player", user, users)

            loot_gained = award_hunt_loot(int(mob_data[0]), party, users)
            loot_message = ""
            if loot_gained is not None:
                for loot in loot_gained:
                    loot_message += f"{loot[1]} {loot[0]}\n"

            start_update_csv(users)
            new_event = [turn, battle_type, party, user_data, mob_data]
            events = update_events_csv(new_event, events, 'delete')
            return [f"You defeated {mob_data[1]}:\n"
                    f"Each Player Looted:\n"
                    f"{coins_gained} money\n"
                    f"{xp_gain} Player XP\n"
                    f"{huntP_gain} HuntPoint\n"
                    f"{loot_message}", events]

        mob_attacks = 0
        esc_counter = 0
        while True:
            # turn counter
            turn += 1
            if turn == len(party):
                turn = 0

            piercing_attack = False
            dodged = False
            # mob attack on turn reset
            if turn == 0:
                # find next alive or last
                mob_damage = 0
                mob_attacks += 1
                piercing_attack = False
                if random.randint(1, 12) == 1:
                    piercing_attack = True

                enemy_damage = random.randint(int(mob_data[4]) - 1, int(mob_data[4]) + 1)
                most_hp = 0
                biggest_hp_amount = 0
                for pos in range(len(party)):
                    if int(user_data[pos][1]) > biggest_hp_amount and int(user_data[pos][0]) > 0:
                        most_hp = pos
                        biggest_hp_amount = user_data[pos][1]

                dodged = True
                if random.randint(1, 100) > user_data[most_hp][4]:
                    dodged = False

                if not dodged:
                    mob_damage += enemy_damage
                    if not piercing_attack:
                        for _ in range(enemy_damage):
                            if user_data[most_hp][2] > 0:
                                user_data[most_hp][2] -= 1
                            else:
                                user_data[most_hp][0] -= 1
                    if piercing_attack:
                        user_data[most_hp][0] -= enemy_damage

            # test players dead
            members_dead = 0
            for pos in range(len(party)):
                if user_data[pos][0] <= 0:
                    members_dead += 1
            if members_dead == len(party):
                coins_lost = round(int(mob_data[5]) * 3, 2)
                for user in users:
                    for player in party:
                        if user.user_id == player[0]:
                            if user.bal < coins_lost:
                                user.bal = 0
                            user.bal -= coins_lost
                start_update_csv(users)
                new_event = [turn, battle_type, party, user_data, mob_data]
                events = update_events_csv(new_event, events, 'delete')
                return [
                    f"You were defeated by {mob_data[1]}:\n They stole £{coins_lost} from each party member",
                    events]

            # test if next turn valid
            if int(user_data[turn][0]) > 0 and int(user_data[turn][6]) == 0:
                break

            # attack cool down
            if user_data[turn][6] > 0:
                user_data[turn][6] -= 1

            # loop break out error
            if esc_counter > 10:
                new_event = [turn, battle_type, party, user_data, mob_data]
                events = update_events_csv(new_event, events, 'delete')
                return [
                    f"The event timed out due to an error, it has been deleted please start a new one.", events]
            esc_counter += 1







        # can player draw extra card
        if extra_draw:
            new_draw = draw_card_deck(party[turn][0], users, 4)
        else:
            new_draw = draw_card_deck(party[turn][0], users)
        user_data[turn][3] = new_draw

        info = [damage_dealt,
                self_damage,
                shield_gained,
                extra_draw,
                heal_gained,
                extra_draw,
                dodge,
                mob_damage,
                cool_down,
                mob_attacks,
                crit
                ]

        new_event = [turn, battle_type, party, user_data, mob_data]

        start_update_csv(users)
        events = update_events_csv(new_event, events, 'update')

        if dodged:
            return [create_battle_gui(new_event, False, info, "dodged"), events]
        if piercing_attack:
            return [create_battle_gui(new_event, False, info, "pierce"), events]
        else:
            return [create_battle_gui(new_event, False, info), events]
    else:
        return "not your turn"
