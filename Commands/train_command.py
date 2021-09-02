from Commands.update_skills import give_xp
import random


def train_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    # adds TrainingPoints to inv if the user has never had any
    if 'TrainingPoint' not in args[0].inv:
        args[0].inv['TrainingPoint'] = 0

    if int(args[0].inv['TrainingPoint']) > 0:
        points_used = 1  # default amount of points
        if len(args[3]) > 0:  # if user specifies point amount to use
            try:
                # couple of tests to stop (more points used than have or less than 1 used)
                points_used = int(args[3][0])
                if points_used > int(args[0].inv['TrainingPoint']):
                    points_used = int(args[0].inv['TrainingPoint'])
                if points_used < 1:
                    points_used = 1
            except:
                points_used = 1
        random_xp = 0
        for point in range(points_used):
            random_xp += random.randint(50, 60)  # sets xp to gain
        args[0].inv['TrainingPoint'] -= points_used
        give_xp(random_xp, "Player", args[0], args[2])

        return f"Used {points_used} TrainingPoints:\nGained {random_xp} player xp."
    else:
        return 'Must have at least 1 TrainingPoint'
