def start_update_csv(users):
    f = open("users.csv", 'w').close  # clear file
    f = open("users.csv", 'a')
    for user in users:
        f.write(f"{user.user_id} {user.username}*{user.bal}*{user.inv}*{user.skills}*{user.job} {user.pay}\n")
    f.close()