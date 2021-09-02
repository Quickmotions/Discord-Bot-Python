def stats_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    response = f"{args[0].username}s Skill List:\n--------------------"

    for item, value in args[0].skills.items():
        if item == "Player":
            spaces = " " * (9 - len(item))
            response += f"\n{item}:  {spaces} {value[0]}/200,  XP: {value[1]}/{value[2]}\nSkillPoints: {value[3]}\n"
        elif item in ['Fishing', 'Mining', 'Woodcut']:
            spaces = " " * (9 - len(item))
            response += f"\n{item}:  {spaces} {value[0]}/50 + ({args[0].equipment_stats[item]}🛡️)  XP: {value[1]}/{value[2]}"
        else:
            spaces = " " * (9 - len(item))
            response += f"\n{item}:  {spaces} {value}/50 + ({args[0].equipment_stats[item]}🛡️)"

    response += f"\n\n💗️: {round(100 * (1 + (0.1 * (args[0].skills['Health'] + args[0].equipment_stats['Health']))))}"
    response += f"\n💵: {round(args[0].bal, 2)}"
    response += f"\n🔨: {args[0].gathering}"
    return response
