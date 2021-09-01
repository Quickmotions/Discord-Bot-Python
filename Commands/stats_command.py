def stats_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    response = f"{args[0].username}s Skill List:\n--------------------"

    for item, value in args[0].skills.items():
        response += f"\n{item} : Level: {value[0]} ({args[0].equipment_stats[item]}🛡️), XP: {value[1]}/{value[2]}"

    response += f"\n\n💗️: {round(100 * (1 + (0.06 * (args[0].skills['Health'][0] + args[0].equipment_stats['Health']))))}"
    response += f"\n💵: {args[0].bal}"
    response += f"\n🔨: {args[0].gathering}"
    return response
