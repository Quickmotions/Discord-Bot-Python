from datetime import datetime, timedelta
import random
from Commands.update_csv import start_update_quests, start_update_csv

items = [
    ["Cod", 40],
    ["Mackerel", 40],
    ["Carp", 40],
    ["Trout", 40],
    ["Salmon", 40],
    ["Catfish", 40],
    ["Tuna", 40],
    ["Stone", 20],
    ["Limestone", 25],
    ["Basalt", 30],
    ["IronOre", 50],
    ["TinOre", 50],
    ["GoldOre", 70],
    ["Ruby", 100],
    ["Sapphire", 100],
    ["Diamond", 100],
    ["Coal", 20],
    ["TinIngot", 100],
    ["IronIngot", 100],
    ["Leather", 20],
    ["GoldIngot", 140],
    ["DarkShard", 50],
    ["Ectoplasm", 40],
    ["HelixCore", 300],
    ["ShadeWoodLog", 100],
    ["BlackLeather", 100],
    ["DevilIngot", 300],
    ["Coal", 20],
    ["MithrilIngot", 180],
    ["TitaniumIngot", 380],
    ["Blood", 30],
    ["AncientRune", 76],
    ["Bone", 25],
    ["OakLog", 40],
    ["SpruceLog", 40],
    ["PineLog", 40],
    ["BeechLog", 40],
    ["MapleLog", 40],
    ["AshLog", 40],
    ["Paper", 75],
    ["CutStone", 40],
    ["CutLimestone", 50],
    ["CutBasalt", 60],
    ["RemovalSigil", 1000],
    ["WaterRune", 100],
    ["AirRune", 220],
    ["IceRune", 350],
    ["FireRune", 500],
    ["HallowedHelmet", 2000],
    ["HallowedChestplate", 2000],
    ["HallowedLeggings", 2000],
    ["HallowedBoots", 2000],
    ["HallowedSpear", 2000],

]


class Quests:
    def __init__(self, info, start, cost, reward, users_list):
        self.info = str(info)
        self.start = datetime.strptime(str(start), '%Y-%m-%d %H:%M:%S.%f')
        self.cost = str(cost)
        self.reward = str(reward)
        users = users_list.split('*')
        self.users = []
        for user in users:
            if user != '\n' and user != '':
                self.users.append(user)


def quest_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    quests = setup_quests()

    # test to see if quests are valid today.
    if datetime.today() > (timedelta(days=1) + quests[0].start):
        # setup new daily quests
        new_quests()
        quests = setup_quests()  # set new quest list object

    if len(args[3]) > 0:
        if args[3][0].lower() == 'list':
            quest_list = f"Today's quests ({quests[0].start.strftime('%Y-%m-%d')})\n"
            quest_num = 1
            for quest in quests:
                quest_list += f"{quest_num} - {quest.info}\n"
                quest_num += 1
            return quest_list
        elif args[3][0] == '1' or args[3][0] == '2' or args[3][0] == '3':
            quest = quests[int(args[3][0]) - 1]  # -1 accounts for the list starting at 0

            # test if users already done quest
            for user in quest.users:
                if str(args[0].user_id) == str(user):
                    return f"You have already completed this quest today."

            quest_input_amount, quest_input = quest.cost.split(' ')
            quest_input_amount = int(quest_input_amount)

            # setup between money or item reward
            if len(quest.reward.split(' ')) > 1:
                quest_output_amount, quest_output = quest.reward.split(' ')
                quest_output_amount = int(quest_output_amount)
                quest_type = 'item'
            else:
                quest_output_value = int(quest.reward)
                quest_type = 'money'

            user_inv = args[0].inv

            if quest_input in user_inv:
                if user_inv[quest_input] >= quest_input_amount:
                    user_inv[quest_input] -= quest_input_amount
                    if quest_type == 'item':
                        if quest_output not in user_inv:
                            user_inv[quest_output] = 0
                        user_inv[quest_output] += quest_output_amount
                    else:
                        args[0].bal += quest_output_value

                    quest.users.append(str(args[0].user_id))
                    start_update_csv(args[2])
                    start_update_quests(quests)
                    if quest_type == 'item':
                        return f"You completed quest {args[3][0]} today:\n You lost {quest_input_amount} " \
                           f"{quest_input} and gained {quest_output_amount} {quest_output}."
                    else:
                        return f"You completed quest {args[3][0]} today:\n You lost {quest_input_amount} " \
                               f"{quest_input} and gained £{quest_output_value}."

            return f"You don't own {quest_input_amount} {quest_input} to complete this quest"
        else:
            return f"Incorrect use of Quest command:\ntry 'quest list' or 'quest (1, 2 or 3)' to hand them in"
    return f"Incorrect use of Quest command:\ntry 'quest list' or 'quest (1, 2 or 3)' to hand them in"


def setup_quests():
    quests = []
    f = open('Quests/quest.csv', 'r')
    for quest_data in f.readlines():
        quest_data = quest_data.split(',')
        quests.append(Quests(quest_data[0], quest_data[1], quest_data[2], quest_data[3], quest_data[4]))
    return quests


def new_quests():
    quests = []
    quest_value = 0
    for _ in range(3):  # create 3 quests each day
        quest_value += random.randint(300, 2000)  # value for reward and price of the quest
        item_chosen = ['None', 999999]  # empty base item
        # only select item which is worth less than the quest value so you cant get 0 item
        while item_chosen[1] > quest_value:
            item_chosen = random.choice(items)

        # finds how many of selected item is needed to get close to the value
        required_item = item_chosen[0]
        required_amount = round(quest_value / item_chosen[1])

        # make the reward randomly worth more or less than the quest requirement
        reward_value = round(quest_value * (1 + (0.1 * random.randint(8, 30))))

        reward_choice = ['None', 999999]
        # repeat same as above but for the reward
        while reward_choice[1] > quest_value:
            reward_choice = random.choice(items)
        item_reward = reward_choice[0]
        amount_item_reward = round(quest_value / reward_choice[1])
        reward_value = round(reward_value * 1.2)
        # 2/1 ratio of money reward to item reward quests
        options = [
            f"Gather {required_amount} {required_item}. Reward: £{reward_value}",
            f"Hand in {required_amount} {required_item}. Reward: £{reward_value}",
            f"Fetch {required_amount} {required_item}. Reward: £{reward_value}",
            f"Gather {required_amount} {required_item}. Reward: £{reward_value}",
            f"Gather {required_amount} {required_item}. Reward: {amount_item_reward} {item_reward}",
            f"Fetch {required_amount} {required_item}. Reward: {amount_item_reward} {item_reward}",
            f"Hand in {required_amount} {required_item}. Reward: {amount_item_reward} {item_reward}"
        ]
        # sets start time as current date
        current_time = datetime.today().strftime('%Y-%m-%d')  # just date no time
        current_time += " 00:00:00.000009"
        quest_info = random.randint(0, 6)  # random quest info in options

        if quest_info <= 5:  # money rewards
            quests.append(Quests(options[quest_info], current_time, f"{required_amount} {required_item}", f"{reward_value}", "*"))
        else:  # item rewards
            quests.append(Quests(options[quest_info], current_time, f"{required_amount} {required_item}", f"{amount_item_reward} {item_reward}", "*"))
    start_update_quests(quests)
