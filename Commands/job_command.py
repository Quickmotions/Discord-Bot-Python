def update_user_data(data):
    from Commands.update_csv import start_update_csv
    start_update_csv(data)


def job_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    # work command options: job get, job check, job work, job quit
    if len(args[3]) > 0:  # test for at least 1 arg

        if args[3][0] == "get":
            if args[0].job == "None":
                if len(args[3]) > 1:

                    # add all words after get as the job title
                    job_title = ""
                    for item in args[3][1:]:
                        job_title += str(item) + "-"  # adds a space after each word
                    job_title = job_title[:-1]  # removes the last space

                    # job title length check
                    if len(job_title) > 30:
                        return "Job name too long at max 30 characters"

                    args[0].job = str(job_title).title()

                    # give random start pay
                    import random
                    args[0].pay = float(random.randint(80, 100))

                    update_user_data(args[2])

                else:
                    return "You need to write the job title you want"
            else:

                return "You already have a job, \nType job work instead"

        elif args[3][0] == "quit":
            if args[0].job != "None":
                args[0].job = "None"
                args[0].pay = 0

                update_user_data(args[2])

        elif args[3][0] == "check":
            for user in args[2]:
                if len(args[3]) > 1:
                    if args[3][1] == f"<@!{user.user_id}>":
                        return f"{user.username}s Job Info:\nTitle:\t{user.job}\nPay:\t{user.pay}"

            return f"{args[0].username}s Job Info:\nTitle:\t{args[0].job}\nPay:\t{args[0].pay}"

        elif args[3][0] == "work":
            # need cooldown timer module for this to work
            args[0].bal += args[0].pay

            update_user_data(args[2])
            pass

        else:
            return "Incorrect argument, \nMust be: get, work, quit or check"
