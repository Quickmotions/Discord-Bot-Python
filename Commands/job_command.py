import random
import datetime


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
                    args[0].pay = float(random.randint(40, 60))

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
        elif args[3][0] == "promote":
            if args[0].job != "None":
                if 'WorkPoint' not in args[0].inv:
                    args[0].inv['WorkPoint'] = 0
                if args[0].inv['WorkPoint'] >= args[0].promotion:
                    pay_rise = random.randint(15, 20)
                    args[0].pay += pay_rise

                    args[0].inv['WorkPoint'] -= args[0].promotion
                    args[0].promotion = round(args[0].promotion * 1.12)
                    update_user_data(args[2])
                    return f"You gained a promotion for {round(args[0].promotion / 1.12)} WorkPoints:\nYou gained a " \
                           f"pay increase of £{pay_rise}, bringing your pay up to £{args[0].pay}."

                else:
                    return f"You need {args[0].promotion} WorkPoints in order to gain a promotion:\n" \
                           f"Use 'work' to get some."
        else:
            return "Incorrect argument,\nUse job get (title), job check, job promote or job quit"

    else:
        return "Incorrect argument,\nUse job get (title), job check, job promote or job quit"


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
        tp_earned = round(amount_earned / 15)
        wp_earned = round(duration_in_hour * random.randint(13, 15))

        # adds TrainingPoints to inv if the user has never had any
        if 'TrainingPoint' not in args[0].inv:
            args[0].inv['TrainingPoint'] = 0
        if 'WorkPoint' not in args[0].inv:
            args[0].inv['WorkPoint'] = 0

        # add items gained
        args[0].inv['TrainingPoint'] += tp_earned
        args[0].inv['WorkPoint'] += wp_earned

        args[0].bal += amount_earned

        # reset last time worked
        args[0].last_work = current_time

        update_user_data(args[2])
        return f"You worked for {round(duration_in_hour, 2)} hours:\nYou earned £{amount_earned}.\n+{tp_earned} " \
               f"TrainingPoints\n+{wp_earned} WorkPoints"
    else:
        return "You need a job first, \nTry job get (job title)"
