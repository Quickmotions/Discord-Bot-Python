def skill_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    response = f"{args[0].username}s Skill List:\n--------------------"

    for item, value in args[0].skills.items():
        response += f"\n{item} : Level: {value[0]}, XP: {value[1]}/{value[2]}"

    return response
