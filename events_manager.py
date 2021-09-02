from Commands.update_csv import start_update_events, start_update_csv
import random
import ast
from Mobs.mob_loot import award_hunt_loot
from Commands.update_skills import give_xp




class Events:
    def __init__(self, user, active, mob_name, mob_hp, mob_dmg, draw, shield, hp, max_hp, mob_coins, difficulty):
        self.difficulty = difficulty
        user_stuff = user.split(' ')
        self.user_id = str(user_stuff[0])
        self.username = str(user_stuff[1])
        self.active = str(active)
        self.mob_name = str(mob_name)
        self.mob_hp = int(mob_hp)
        self.mob_max_hp = int(mob_hp)
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
                event.difficulty = mob[0]
                draw = draw_card_deck(user)
                event.draw = draw

                event.shield = 0

                # set up health
                health_base = user.skills['Health'] + user.equipment_stats['Health']
                magic_base = user.skills['Magic'] + user.equipment_stats['Magic']
                critical_base = user.skills['Critical'] + user.equipment_stats['Critical']

                event.max_hp = round(100 * ((((6 * health_base) - (2 * magic_base) - (1 * critical_base)) / 100) + 1))
                if event.max_hp < 1:
                    event.max_hp = 1
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
        items.append(Events(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10]))
    return items  # return list of users (classes)


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
                                            f"❤️: {event.mob_hp} - {info[0]}\n🗡️: Dodged",
                                f"{draw_menu}"]

                    if not piercing_attack:
                        return ["multiple", f"{args[0].username}:\n❤️: {event.hp} - {enemy_damage} + {healing}\n🛡️:"
                                        f" {event.shield} + {info[1]}\n🗡️: {info[0]}\n{event.mob_name}:\n"
                                        f"❤️: {event.mob_hp} - {info[0]}\n🗡️: {enemy_damage}",
                                        f"{draw_menu}"]
                    else:
                        return ["multiple", f"{args[0].username}:\n❤️: {event.hp} - 🪡{enemy_damage} + {healing}\n🛡️:"
                                            f" {event.shield} + {info[1]}\n🗡️: {info[0]}\n{event.mob_name}:\n"
                                            f"❤️: {event.mob_hp} - {info[0]}\n🗡️: {enemy_damage}",
                                f"{draw_menu}"]

    return None
