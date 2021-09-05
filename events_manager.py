from Commands.update_csv import start_update_csv
from datetime import datetime
import random
import ast
from Mobs.mob_loot import award_hunt_loot
from Commands.update_skills import give_xp


class Events:
    def __init__(self, user_party, user_data, mob_data):
        # new event: Event_time, user_party, user_data, mob_data
        self.time = datetime.today()
        for user in user_party:


        for data in user_data:





        user, active, mob_name, mob_hp, mob_max_hp, mob_dmg, draw, shield, hp, max_hp, mob_coins, difficulty = event
        self.difficulty = difficulty
        user_stuff = user.split(' ')
        self.user_id = str(user_stuff[0])
        self.username = str(user_stuff[1])
        self.active = str(active)
        self.mob_name = str(mob_name)
        self.mob_hp = int(mob_hp)
        self.mob_max_hp = int(mob_max_hp)
        self.mob_dmg = int(mob_dmg)
        self.draw = ast.literal_eval(draw)
        self.shield = int(shield)
        self.hp = int(hp)
        self.max_hp = int(max_hp)
        self.mob_coins = float(mob_coins)


def setup_events():
    events = []
    f = open("events.csv", "r")
    for event in f.readlines():
        event = event.strip()
        event = event.split('*')
        events.append(event)


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


def start_combat(user, users, mob, battle_type, events):
    user_party = user.party
    for event in events:
        if event.user_id == user.user_id:
            if event.active == "Active=Yes":
                return f"You already have an active combat:\nComplete the event first."

    event_data = []
    # new event: Event_time, user_party, user_data, mob_data
    event_data.append(datetime.now())
    event_data.append(user_party)
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

                user_data.append(hp, max_hp, 0, draw_card_deck(user))
    event_data.append(user_data)

    difficulty = mob[0]
    mob_name = mob[1]
    mob_hp = mob[2]
    mob_max_hp = mob[2]
    mob_dmg = mob[3]
    mob_coins = mob[4]

    event_data.append([difficulty, mob_name, mob_hp, mob_max_hp, mob_dmg, mob_coins])

        user_data.append()
        uid = user.user_id
        uname = user.username





    f = open("events.csv", 'a')

            f"{event.active}*{event.mob_name}*"
            f"{event.mob_hp}*{event.mob_max_hp}*"
            f"{event.mob_dmg}*"
            f"{event.draw}*"
            f"{event.shield}*"
            f"{event.hp}*"
            f"{event.max_hp}*"
            f"{event.mob_coins}*"
            f"{event.difficulty}\n")
    f.close()



    if battle_type == 'PVE':
        for event in events:
            if event.user_id == user.user_id:
                event.active = "Active=Yes"

                draw = draw_card_deck(user)
                event.draw = draw

                event.shield = 0


                draw_menu = "Your Cards:\n"
                num = 1
                for card in draw:
                    draw_menu += f"{num} = {card}\n"
                    num += 1

                return ["multiple", f"Combat started with {mob[1]}:",
                        f"{user.username}:\n❤️: {event.hp}\n🛡️:"
                        f" {event.shield}\n{event.mob_name}:\n"
                        f"❤️: {event.mob_hp}\n🗡️: {event.mob_dmg}",
                        f"{draw_menu}"]

                return ["event",
                        f"Combat started with {mob[1]}:\nMob HP: {mob[2]}\nMob DMG: {mob[3]}\nYour attacks: {draw}"]


def check_event_response(*args):
    # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list 4 = events 5 = input message
    events = setup_events()









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
