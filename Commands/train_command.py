def train_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        # adds training points to inv if the user has never had any
        if 'Training Point' not in args[0].inv:
            args[0].inv['Training Point'] = 0

        if int(args[0].inv['Training Point']) > 0:
            skill_to_train = (args[3][0]).title()
            if skill_to_train in args[0].skills:  # check if skill exists
                points_used = 1  # default amount of points
                if len(args[3]) > 1:  # if user specifies point amount to use
                    try:
                        # couple of tests to stop (more points used than have or less than 1 used)
                        points_used = int(args[3][1])
                        if points_used > int(args[0].inv['Training Point']):
                            points_used = int(args[0].inv['Training Point'])
                        if points_used < 1:
                            points_used = 1

                    finally:  # if user inputs invalid point amount leave amount as one
                        pass

                from Commands.update_skills import give_xp
                import random
                random_xp = 0
                for point in range(points_used):
                    random_xp += random.randint(20, 100)  # sets xp to gain
                args[0].inv['Training Point'] -= points_used
                give_xp(random_xp, skill_to_train, args[0], args[2])

                return f"Used {points_used} Training Points:\nGained {random_xp} xp in {skill_to_train}"

            else:
                return "Skill not found in list:\nUse 'skill' command to see all skills"
        else:
            return 'Must have at least 1 training point'
    else:
        return "Incorrect use of train command\nUse train (skill) (optional: amount of points to spend)"
