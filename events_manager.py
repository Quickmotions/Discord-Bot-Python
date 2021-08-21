from Commands.update_csv import start_update_events, start_update_csv
import random
import ast


class Events:
    def __init__(self, user, active, mob_name, mob_hp, mob_dmg, draw, shield, hp, max_hp, mob_coins):
        user_stuff = user.split(' ')
        self.user_id = str(user_stuff[0])
        self.username = str(user_stuff[1])
        self.active = str(active)
        self.mob_name = str(mob_name)
        self.mob_hp = int(mob_hp)
        self.mob_dmg = int(mob_dmg)
        self.draw = ast.literal_eval(draw)
        self.shield = int(shield)
        self.hp = int(hp)
        self.max_hp = int(max_hp)
        self.mob_coins = float(mob_coins)


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
    events = get_data()
    for event in events:
        if event.user_id == user.user_id:
            if event.active == "Active=Yes":
                return f"You already have an active combat:\nComplete or quit the event first."
    if battle_type == 'PVE':
        for event in events:
            if event.user_id == user.user_id:
                event.active = "Active=Yes"
                event.mob_name = mob[1]
                event.mob_hp = mob[2]
                event.mob_dmg = mob[3]
                event.mob_coins = mob[4]

                draw = draw_card_deck(user)
                event.draw = draw
                event.hp = event.max_hp

                start_update_events(events)

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


def get_data():
    items = []
    f = open("events.csv", "r")
    for item in f.readlines():
        item = item.strip()  # remove \n
        item = item.split('*')  # split into items
        # create class for each user
        items.append(Events(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9]))
    return items  # return list of users (classes)


def use_card(card, user, event):
    combat = 1 + (0.1 * user.skills['Combat'][0])
    defense = 1 + (0.1 * user.skills['Defense'][0])
    damage_dealt = 0
    shield_gained = 0
    extra_draw = False

    if card == "Slash":
        damage_dealt = round(3 * combat)
    if card == "Defend":
        shield_gained = round(10 * defense)
    if card == "Charge":
        damage_dealt = round(1 * combat)
        extra_draw = True

    event.mob_hp -= damage_dealt
    event.shield += shield_gained
    return [damage_dealt, shield_gained, extra_draw]


def check_event_response(*args):
    # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list 4 = events 5 = input message
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

                    info = use_card(draw[choice], args[0], event)

                    if info[2]:  # can player draw extra card
                        new_draw = draw_card_deck(args[0], 4)
                    else:
                        new_draw = draw_card_deck(args[0])

                    # enemy turn
                    if event.mob_hp <= 0:  # is mob dead?
                        event.active = "Active=No"
                        start_update_events(args[4])

                        coins_gained = float(event.mob_coins) / 100
                        coins_gained = round(coins_gained * random.randint(90, 110), 2)
                        tp_gain = round(event.mob_coins / random.randint(6, 14))

                        args[0].bal += coins_gained

                        if 'Training Point' not in args[0].inv:
                            args[0].inv['Training Point'] = 0
                        args[0].inv['Training Point'] += tp_gain
                        start_update_csv(args[2])
                        start_update_events(args[4])
                        return f"You defeated {event.mob_name}:\n You looted £{coins_gained} and {tp_gain} Training Points from it"

                    enemy_damage = random.randint(event.mob_dmg - 1, event.mob_dmg + 1)

                    for _ in range(enemy_damage):
                        if event.shield > 0:
                            event.shield -= 1
                        else:
                            event.hp -= 1

                    if event.hp <= 0:
                        event.active = "Active=No"
                        start_update_events(args[4])
                        coins_lost = event.mob_hp
                        if args[0].bal < coins_lost:
                            coins_lost = args[0].bal
                        args[0].bal -= coins_lost
                        start_update_csv(args[2])
                        start_update_events(args[4])
                        return f"You were defeated by {event.mob_name}:\n They stole £{coins_lost} from you"

                    event.draw = new_draw
                    start_update_events(args[4])

                    draw_menu = "Your Cards:\n"
                    num = 1
                    for card in new_draw:
                        draw_menu += f"{num} = {card}\n"
                        num += 1

                    return ["multiple", f"{args[0].username}:\n❤️: {event.hp} - {enemy_damage}\n🛡️:"
                                        f" {event.shield} + {info[1]}\n🗡️: {info[0]}\n{event.mob_name}:\n"
                                        f"❤️: {event.mob_hp} - {info[0]}\n🗡️: {enemy_damage}",
                                        f"{draw_menu}"]

    return None
