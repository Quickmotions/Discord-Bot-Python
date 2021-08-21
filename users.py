import ast
from datetime import datetime


class Player:
    def __init__(self, user_id, bal, inv, skills, job, last_work, cards, gathering, gathering_time):
        u_id, username = user_id.split(' ', 1)
        self.user_id = str(u_id)
        self.username = str(username)
        self.bal = round(float(bal), 2)
        self.inv = ast.literal_eval(inv)
        self.skills = ast.literal_eval(skills)
        self.job = str(job)
        job, pay = job.split(' ')
        self.job = str(job)
        self.pay = float(pay)
        if last_work != "None":
            self.last_work = datetime.strptime(str(last_work), '%Y-%m-%d %H:%M:%S.%f')
        else:
            self.last_work = "None"
        self.cards = ast.literal_eval(cards)
        self.gathering = gathering
        if gathering_time != "None":
            self.gathering_time = datetime.strptime(str(gathering_time), '%Y-%m-%d %H:%M:%S.%f')
        else:
            self.gathering_time = "None"

    def change_bal(self, val):
        self.bal += val
        # update csv with new bal

    def change_inv(self, val, item_name):
        self.inv[item_name] += val
        # update csv with new inv


def get_data():
    items = []
    f = open("users.csv", "r")
    for item in f.readlines():
        item = item.strip()  # remove \n
        item = item.split('*')  # split into items
        # create class for each user
        items.append(Player(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8]))
    return items  # return list of users (classes)


def run_setup_users():
    users = get_data()  # list of classes
    return users
