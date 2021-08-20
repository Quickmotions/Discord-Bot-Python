def start_update_csv(users):
    f = open("users.csv", 'w').close  # clear file
    f = open("users.csv", 'a')
    for user in users:
        f.write(f"{user.user_id} {user.username}*{user.bal}*{user.inv}*{user.skills}*{user.job} {user.pay}\n")
    f.close()


def start_update_cooldown(cds):
    f = open("cooldowns.csv", 'w').close  # clear file
    f = open("cooldowns.csv", 'a')
    for cd in cds:
        f.write(f"{cd.cool_down_end}*{cd.command}*{cd.user_id}\n")
    f.close()


def start_update_events(events):
    f = open("events.csv", 'w').close  # clear file
    f = open("events.csv", 'a')
    for event in events:
        f.write()
    f.close()
