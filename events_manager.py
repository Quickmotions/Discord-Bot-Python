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
            for user_id, username, membership in user_party:
                if user_id == str(member[0]):
                    return f"{username} already has an active combat:\nThey need to complete their event first."

    event_data = [0, battle_type, user_party]
    user_data = []

    for member in user_party:
        for user in users:
            if user.user_id == member[0]:
                # set up health and dodge
                health_base = user.skills['Health'] + user.equipment_stats['Health']
                magic_base = user.skills['Magic'] + user.equipment_stats['Magic']
                critical_base = user.skills['Critical'] + user.equipment_stats['Critical']
                dodge_base = user.skills['Dodge'] + user.equipment_stats['Dodge']
                agility_base = user.skills['Agility'] + user.equipment_stats['Agility']
                defense_base = user.skills['Defense'] + user.equipment_stats['Defense']

                dodge = ((0.5 * dodge_base) + (0.2 * agility_base) - (0.25 * defense_base))

                max_hp = round(100 * ((((6 * health_base) - (2 * magic_base) - (1 * critical_base)) / 100) + 1))
                if max_hp < 1:
                    max_hp = 1
                hp = max_hp



                user_data.append([hp, max_hp, 0, draw_card_deck(user), 0, dodge])
    if len(user_data) > 1:
        user_data.reverse()
    event_data.append(user_data)
    event_data.append([mob[0], mob[1], mob[2], mob[2], mob[3], mob[4]])

    # info about EVENT_DATA: ----------------------------
    # turn, battle_type, party, user_data, mob_data
    # ---------------------------------------------------
    # party = [user_id, username, 'member/invite'] * party
    # user_data = [hp, maxhp, shield, draw, dodge, reg_dodge] * party
    # mob_data = [difficulty, name, hp, maxhp, dmg, coins]
    # ---------------------------------------------------

    update_events_csv(event_data, events, 'append')

    gui = create_battle_gui(event_data, True)
    return gui


def create_draw_gui(draw):
    count = 1
    gui = ""
    for card in draw:
        gui += f"{count} - {card}\n"
        count += 1
    return gui


def create_battle_gui(event_data, start, info=[], extra="None"):
    turn, battle_type, party, user_data, mob = event_data
    mob_hp_percent = round((100 / int(mob[3])) * int(mob[2]))

    if len(info) > 0:
        damage_dealt, self_damage, shield_gained, extra_draw, heal_gained, extra_draw, dodge = info
        if extra == "pierce":
            mob[4] = "🪡" + mob[4]
        if extra == "no_attack":
            mob[4] = 0
        if extra == "dodged":
            mob[4] = "Dodged"
        user_data[turn][4] = dodge


    gui = ["multiple"]
    players_gui = ""

    if start:
        for pos in range(len(party)):
            players_gui += f"{party[pos][1]}:\n" \
                           f"💗: {user_data[pos][0]}/{user_data[pos][1]}\n" \
                           f"🛡️: {user_data[pos][2]}\n"
    else:
        for pos in range(len(party)):
            player_hp_percent = round((100 / user_data[pos][1]) * user_data[pos][0])
            players_gui += f"{party[pos][1]}:\n" \
                           f"💗: {user_data[pos][0]}/{user_data[pos][1]} ({player_hp_percent}%) + {heal_gained}\n" \
                           f"🛡️: {user_data[pos][2]} + {shield_gained}\n" \
                           f"🗡️: {damage_dealt}\n" \


    if start:
        players_gui += f"{mob[1]}:\n" \
                       f"💗: {mob[2]}/{mob[3]}\n" \
                       f"🗡️: {mob[4]}"
    else:
        players_gui += f"{mob[1]}:\n" \
                       f"💗: {mob[2]}/{mob[3]} ({mob_hp_percent}%) - {damage_dealt}\n" \
                       f"🗡️: {mob[4]}"

    gui.append(players_gui)
    gui.append(f"{party[turn][1]}s Turn:\n{create_draw_gui(user_data[turn][3])}")
    return gui


def check_event_response(*args):
    # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list 4 = events 5 = input message
    if args[4] == "1" or args[4] == "2" or args[4] == "3" or args[4] == "4":
        events = get_events()
        for event in events:
            for member in event[2]:
                if str(member[0]) == args[0].user_id:
                    turn, battle_type, party, user_data, mob_data = event
                    return battle_turn(turn, battle_type, party, user_data, mob_data, args[0], args[2], args[4], events)


def update_events_csv(event_updated, events, update_type):
    new_events = []
    if update_type == 'append':
        f = open("events.csv", 'a')
        f.write(f'{event_updated}\n')
        f.close()
        return

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
    f = open("events.csv", 'w')
    for event in new_events:
        f.write(f"{event}\n")
    f.close()


def battle_turn(turn, battle_type, party, user_data, mob_data, user, users, response, events):
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

        damage_dealt, self_damage, shield_gained, extra_draw, heal_gained, extra_draw, dodge_bonus \
            = use_card(draw[choice], user, mob_data)

        mob_data[2] = int(mob_data[2])
        user_data[turn][0] = int(user_data[turn][0])
        user_data[turn][2] = int(user_data[turn][2])
        user_data[turn][4] = int(user_data[turn][4])

        mob_data[2] -= damage_dealt
        user_data[turn][0] -= self_damage
        user_data[turn][2] += shield_gained

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


        # can player draw extra card
        if extra_draw:
            new_draw = draw_card_deck(user, 4)
        else:
            new_draw = draw_card_deck(user)

        # enemy turn

        if int(mob_data[2]) <= 0:  # is mob dead?

            coins_gained = int(mob_data[5]) / 100
            coins_gained = round(coins_gained * random.randint(90, 110), 2)
            huntP_gain = round(int(mob_data[5]) / random.randint(2, 5))
            xp_gain = round((coins_gained / 3) * (1 + 0.1 * (random.randint(-4, 4))))

            for user in users:
                for player in party:
                    if user.user_id == player[0]:
                        if user.bal < coins_gained:
                            coins_gained = user.bal
                        user.bal -= coins_gained
                        if 'HuntPoint' not in user.inv:
                            user.inv['HuntPoint'] = 0
                        user.inv['HuntPoint'] += huntP_gain
                        give_xp(xp_gain, "Player", user, users)

            loot_gained = award_hunt_loot(int(mob_data[0]), user, users)
            loot_message = ""
            if loot_gained is not None:
                for loot in loot_gained:
                    loot_message += f"{loot[1]} {loot[0]}\n"

            start_update_csv(users)
            new_event = [turn, battle_type, party, user_data, mob_data]
            update_events_csv(new_event, events, 'delete')
            return f"You defeated {mob_data[1]}:\n" \
                   f"Each Player Looted:\n" \
                   f"{coins_gained} money\n" \
                   f"{xp_gain} Player XP\n" \
                   f"{huntP_gain} HuntPoint\n" \
                   f"Last Hit:\n" \
                   f"{loot_message}"


        piercing_attack = False
        dodged = False
        mob_attacked = False

        turn += 1

        # find next alive or last

        if turn == len(party):
            piercing_attack = False
            if random.randint(1, 12) == 1:
                piercing_attack = True

            enemy_damage = random.randint(int(mob_data[4]) - 1, int(mob_data[4]) + 1)
            most_hp = 0
            for pos in range(len(party)):
                if int(user_data[pos][0]) > 0:
                    if int(user_data[pos][1]) > int(user_data[most_hp][1]):
                        most_hp = pos

            dodged = True
            if random.randint(1, 100) > user_data[most_hp][4]:
                dodged = False

            if not dodged:
                mob_attacked = True
                if not piercing_attack:
                    for _ in range(enemy_damage):
                        if user_data[most_hp][2] > 0:
                            user_data[most_hp][2] -= 1
                        else:
                            user_data[most_hp][0] -= 1
                if piercing_attack:
                    user_data[most_hp][0] -= enemy_damage

            # is player dead test for all members
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
                                coins_lost = user.bal
                            user.bal -= coins_lost
                start_update_csv(users)
                new_event = [turn, battle_type, party, user_data, mob_data]
                update_events_csv(new_event, events, 'delete')
                return f"You were defeated by {mob_data[1]}:\n They stole £{coins_lost} from each party member"


            if turn == len(party):
                turn = 0
            while int(user_data[turn][0]) <= 0:
                turn += 1
                if turn == len(party):
                    turn = 0

        user_data[turn][3] = new_draw

        draw_menu = "Your Cards:\n"
        num = 1
        for card in new_draw:
            draw_menu += f"{num} = {card}\n"
            num += 1



        info = [damage_dealt, self_damage, shield_gained, extra_draw, heal_gained, extra_draw, dodge_bonus]
        new_event = [turn, battle_type, party, user_data, mob_data]

        start_update_csv(users)
        update_events_csv(new_event, events, 'update')

        if dodged:
            return create_battle_gui(new_event, False, info, "dodged")
        if not mob_attacked:
            return create_battle_gui(new_event, False, info, "no_attack")
        if piercing_attack:
            return create_battle_gui(new_event, False, info, "pierce")
        else:
            return create_battle_gui(new_event, False, info)
    else:
        return "not your turn"
