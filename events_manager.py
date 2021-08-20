from Commands.update_csv import start_update_csv

class Events:
    def __init__(self, user, mob, battle_type):
        self.user = user
        self.mob = mob
        self.battle_type = battle_type


def start_combat(user, users, mob, battle_type):
    events = get_data()
    for event in events:
        if event.user_id == user.user_id:
            return f"You already have an active combat:\nComplete or quit the event first."
    if battle_type == 'PVE':
        Events(f"{user.user_id}*{mob.name}")
        start_update_csv()
        return ["event", f"Combat started with {mob[1]}:\nMob HP: {mob[2]}\nMob DMG: {mob[3]}", [user, mob, battle_type]]


def get_data():
    items = []
    f = open("events.csv", "r")
    for item in f.readlines():
        item = item.strip()  # remove \n
        item = item.split('*')  # split into items
        # create class for each user
        items.append(Events())
    return items  # return list of users (classes)


def check_event_response(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    # events = args[4]
    # print(args[0].in_event)
    # if args[0].in_event == "Yes":
    #     # combat
    pass



    print("not")
    return None
