class Player:
    def __init__(self, user_id, bal, inv):

        self.user_id = user_id
        self.bal = bal

        # inventory management
        inventory = {"Wood": 0, "Stone": 0, "Gift": 0}
        inv = inv.split(' ')  # each item in inv as list
        for item in inv:
            item = item.split('.')  # item[0] = name, item[1] = amount
            inventory[str(item[0])] += int(item[1])
        self.inv = inventory


def get_data():
    items = []
    f = open("users.csv", "r")
    for item in f.readlines():
        item = item.strip()  # remove \n
        item = item.split(',')  # split into items
        items.append(Player(item[0], item[1], item[2]))  # create class for each user
    return items  # return list of users (classes)


if __name__ == '__main__':
    users = get_data()  # list of classes
    for user in users:
        print(user.user_id, user.bal, user.inv)

    from command_manager import start
    start(users)
