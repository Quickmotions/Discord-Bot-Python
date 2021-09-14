import ast

from datetime import datetime


class Player:
    def __init__(self, user_id, bal="0.0", inv="{}", skills="{}", job="None 0.0 200", last_work="None", cards="{'Slash': 3, 'Defend': 1, 'Charge': 1}/[]", gathering="gathering=no", gathering_time="None", equipment="{}/{}", party="None", buildings="[]"):
        u_id, username = user_id.split(' ', 1)
        # user data
        self.user_id = str(u_id)
        self.username = str(username)

        # balance
        self.bal = round(float(bal), 2)

        # inv
        self.inv = ast.literal_eval(inv)

        # equipment
        equipment, equipment_stats = equipment.split('/')
        self.equipment = ast.literal_eval(equipment)
        self.equipment_stats = ast.literal_eval(equipment_stats)

        # skills
        self.skills = ast.literal_eval(skills)

        # job
        self.job = str(job)
        job, pay, promotion = job.split(' ')
        self.job = str(job)
        self.pay = float(pay)
        self.promotion = int(promotion)
        if last_work != "None":
            self.last_work = datetime.strptime(str(last_work), '%Y-%m-%d %H:%M:%S.%f')
        else:
            self.last_work = "None"

        # cards

        # adds loadouts if missing
        if cards[-1] != "]":
            cards += "/[]"

        cards = cards.split('/')
        self.loadout = ast.literal_eval(cards[1])
        self.cards = ast.literal_eval(cards[0])
        if len(self.loadout) == 0:
            self.loadout.append(self.cards)

        # buildings
        self.buildings = ast.literal_eval(buildings)

        # gathering
        self.gathering = gathering
        if gathering_time != "None":
            self.gathering_time = datetime.strptime(str(gathering_time), '%Y-%m-%d %H:%M:%S.%f')
        else:
            self.gathering_time = "None"

        # party
        if party == "None":
            self.party = []
            self.party.append([u_id, username, 'member'])
        else:
            self.party = ast.literal_eval(party)




    def change_bal(self, val):
        self.bal += val
        # update csv with new bal

    def change_inv(self, val, item_name):
        self.inv[item_name] += val
        # update csv with new inv


def get_data():
    users = []
    f = open("users.csv", "r")
    for item in f.readlines():
        item = item.strip()  # remove \n
        items = item.split('*')  # split into items
        # create class for each user
        users.append(Player(items[0], items[1], items[2], items[3], items[4], items[5], items[6], items[7], items[8], items[9], items[10], items[11]))
    return users  # return list of users (classes)


def run_setup_users():
    users = get_data()  # list of classes
    return users
