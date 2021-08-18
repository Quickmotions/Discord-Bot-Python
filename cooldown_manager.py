from datetime import datetime


class CoolDowns:
    def __init__(self, cool_down_end, command, user_id, ):
        self.cool_down_end = datetime.strptime(str(cool_down_end), '%Y-%m-%d %H:%M:%S.%f')
        self.command = str(command)
        self.user_id = str(user_id)


def get_data():
    items = []
    f = open("cooldowns.csv", "r")
    for item in f.readlines():
        item = item.strip()  # remove \n
        item = item.split('*')  # split into items
        items.append(CoolDowns(item[0], item[1], item[2]))  # create class for each user
    return items  # return list of users (classes)


def run_setup_cool_down():
    cd = get_data()  # list of classes
    return cd
