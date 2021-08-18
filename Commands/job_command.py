import random


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
                    if len(job_title) > 20:
                        return "Job name too long, max 20 characters"

                    args[0].job = str(job_title).title()

                    # give random start pay
                    import random
                    import datetime
                    args[0].pay = float(random.randint(30, 60))

                    # if user never had a start working time then start it now
                    if args[0].last_work == "None":
                        args[0].last_work = datetime.datetime.today()
                        update_user_data(args[2])

                    update_user_data(args[2])
                    return f"You got hired as {args[0].job}"

                else:
                    return "You need to write the job title you want:\n It can be anything you want."
            else:

                return "You already have a job: \nType work instead"

        elif args[3][0] == "quit":
            if args[0].job != "None":
                args[0].job = "None"
                args[0].pay = 0

                update_user_data(args[2])
                return f"You quit your job as {args[0].job}"

        elif args[3][0] == "check":
            for user in args[2]:
                if len(args[3]) > 1:
                    if args[3][1] == f"<@!{user.user_id}>" or args[3][1] == f"<@{user.user_id}>":
                        return f"{user.username}s Job Info:\nTitle:\t{user.job}\nPay:\t{user.pay}"

            return f"{args[0].username}s Job Info:\nTitle:\t{args[0].job}\nPay:\t{args[0].pay}"

        else:
            return "Incorrect argument,\nUse job get (title), or job check or job quit"

    else:
        return "Incorrect argument,\nUse job get (title), or job check or job quit"


def work_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if args[0].job != 'None':
        from datetime import datetime
        current_time = datetime.today()

        # if user never had a start working time then start it now
        if args[0].last_work == "None":
            args[0].last_work = current_time
            update_user_data(args[2])
            return "Your work has begun:\nWait a while and try again to collect your earnings"

        duration = current_time - args[0].last_work
        duration_in_sec = duration.total_seconds()
        duration_in_hour = duration_in_sec / 60 / 60

        amount_earned = round(args[0].pay * duration_in_hour, 2)
        tp_earned = round(duration_in_hour * 1.5)

        # adds training points to inv if the user has never had any
        if 'Training Point' not in args[0].inv:
            args[0].inv['Training Point'] = 0

        # add items gained
        args[0].inv['Training Point'] += tp_earned
        args[0].bal += amount_earned

        # reset last time worked
        args[0].last_work = current_time

        if random.randint(1, 4) == 1 and duration_in_hour > 2:
            update_user_data(args[2])
            args[0].pay = round(args[0].pay * 1.15, 2)
            update_user_data(args[2])
            return f"You worked for {round(duration_in_hour, 2)} hours:\nYou earned £{amount_earned} and" \
                   f" got {tp_earned} Training Points.\n You also got a promotion, Congrats"

        update_user_data(args[2])
        return f"You worked for {round(duration_in_hour, 2)} hours:\nYou earned £{amount_earned} and" \
               f" got {tp_earned} Training Points."
    else:
        return "You need a job first, \nTry job get (job title)"
