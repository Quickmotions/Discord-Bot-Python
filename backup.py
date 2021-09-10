from datetime import datetime


def start_backup(users):
    time = datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')
    name = f"users_{time}"
    f = open(f"BackUps/{name}.csv", 'w').close  # clear file
    f = open(f"BackUps/{name}.csv", 'a')
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
