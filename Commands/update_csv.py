def start_update_csv(users):
    f = open("users.csv", 'w').close  # clear file
    f = open("users.csv", 'a')
    for user in users:
        f.write(f"{user.user_id} {user.username}*{user.bal}*{user.inv}*{user.skills}*{user.job} {user.pay}*"
                f"{user.last_work}\n")
    f.close()


def start_update_cooldown(cds):
    f = open("cooldowns.csv", 'w').close  # clear file
    f = open("cooldowns.csv", 'a')
    for cd in cds:
        f.write(f"{cd.cool_down_end}*{cd.command}*{cd.user_id}\n")
    f.close()
