def start_update_csv(users):
    f = open("users.csv", 'w').close  # clear file
    f = open("users.csv", 'a')
    for user in users:
        f.write(f"{user.user_id} {user.username}*{user.bal}*{user.inv}*{user.skills}*{user.job} {user.pay} {user.promotion}*{user.last_work}*{user.cards}*{user.gathering}*{user.gathering_time}*{user.equipment}/{user.equipment_stats}\n")
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
        f.write(f"{event.user_id} {event.username}*{event.active}*{event.mob_name}*{event.mob_hp}*{event.mob_dmg}*{event.draw}*{event.shield}*{event.hp}*{event.max_hp}*{event.mob_coins}*{event.difficulty}\n")
    f.close()


def start_update_quests(quests):
    f = open("Quests/quest.csv", 'w').close  # clear file
    f = open("Quests/quest.csv", 'a')
    for quest in quests:
        user_list = ""
        for user in quest.users:
            user_list += str(user) + '*'
        f.write(f"{quest.info},{quest.start},{quest.cost},{quest.reward},{user_list}\n")
    f.close()
