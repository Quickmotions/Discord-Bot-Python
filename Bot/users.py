import ast


class Player:
    def __init__(self, user_id, bal, inv, skills, job):

        self.user_id = str(user_id)
        self.bal = float(bal)
        self.inv = ast.literal_eval(inv)
        self.skills = ast.literal_eval(skills)
        self.job = str(job)
        job, pay = job.split(' ')
        self.job = str(job)
        self.pay = float(pay)

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
        items.append(Player(item[0], item[1], item[2], item[3], item[4]))  # create class for each user
    return items  # return list of users (classes)


if __name__ == '__main__':
    users = get_data()  # list of classes
    for user in users:
        print(user.user_id, user.bal, user.inv, user.skills, user.job, user.pay)

    from command_manager import start
    start(users)
