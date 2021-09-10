def start_update_csv(users):
    f = open("users.csv", 'w').close  # clear file
    f = open("users.csv", 'a')
    for user in users:
        f.write(f"{user.user_id} {user.username}*"
                f"{user.bal}*"
                f"{user.inv}*"
                f"{user.skills}*"
                f"{user.job} {user.pay} {user.promotion}*"
                f"{user.last_work}*"
                f"{user.cards}*"
                f"{user.gathering}*"
                f"{user.gathering_time}*"
                f"{user.equipment}/{user.equipment_stats}*"
                f"{user.party}*"
                f"{user.buildings}\n")
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
        f.write(f"{event.user_id} {event.username}*"
                f"{event.active}*{event.mob_name}*"
                f"{event.mob_hp}*{event.mob_max_hp}*"
                f"{event.mob_dmg}*"
                f"{event.draw}*"
                f"{event.shield}*"
                f"{event.hp}*"
                f"{event.max_hp}*"
                f"{event.mob_coins}*"
                f"{event.difficulty}\n")
    f.close()


def start_update_quests(quests):
    f = open("Quests/quest.csv", 'w').close  # clear file
    f = open("Quests/quest.csv", 'a')
    for quest in quests:
        user_list = ""
        for user in quest.users:
            user_list += str(user) + '*'
        f.write(f"{quest.info},"
                f"{quest.start},"
                f"{quest.cost},"
                f"{quest.reward},"
                f"{user_list}\n")
    f.close()
