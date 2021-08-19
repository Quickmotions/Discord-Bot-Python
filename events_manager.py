from Commands.update_csv import start_update_csv

class Events:
    def __init__(self, user, mob, battle_type):
        self.user = user
        self.mob = mob
        self.battle_type = battle_type


def start_combat(user, users, mob, battle_type, events: list):
    if user.in_event == "Yes":
        return f"You already have an active combat:\nComplete or quit the event first."
    if battle_type == 'PVE':
        user.in_event = "Yes"
        start_update_csv(users)
        return ["event", f"Combat started with {mob[1]}:\nMob HP: {mob[2]}\nMob DMG: {mob[3]}", [user, mob, battle_type]]


def check_event_response(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    events = args[4]
    print(args[0].in_event)
    if args[0].in_event == "Yes":
        # combat






    print("not")
    return None
