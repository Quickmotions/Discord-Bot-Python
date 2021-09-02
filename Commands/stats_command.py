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

    health_base = args[0].skills['Health'] + args[0].equipment_stats['Health']
    magic_base = args[0].skills['Magic'] + args[0].equipment_stats['Magic']
    critical_base = args[0].skills['Critical'] + args[0].equipment_stats['Critical']
    combat_base = args[0].skills['Combat'] + args[0].equipment_stats['Combat']
    defense_base = args[0].skills['Defense'] + args[0].equipment_stats['Defense']
    agility_base = args[0].skills['Agility'] + args[0].equipment_stats['Agility']
    healing_base = args[0].skills['Healing'] + args[0].equipment_stats['Healing']

    combat = ((4 * combat_base) - (2 * defense_base) - (1 * healing_base)) + 100
    defense = (10 * defense_base - 4 * health_base) + 100
    magic = ((10 * magic_base) - (2 * defense_base) - (1 * healing_base)) + 100
    agility = ((6 * agility_base) - (2 * defense_base) - (1 * healing_base)) + 100
    healing = ((10 * healing_base) - (2 * combat_base) - (2 * agility_base) - (2 * magic_base)) + 100
    health = round(100 * ((((6 * health_base) - (4 * magic_base) - (2 * critical_base)) / 100) + 1))

    if combat < 1:
        combat = 1
    if defense < 1:
        defense = 1
    if magic < 1:
        magic = 1
    if agility < 1:
        agility = 1
    if healing < 1:
        healing = 1
    if health < 1:
        health = 1

    response += f"\n\n️❤: {health}hp"
    response += f"    ⚔: {combat}%"
    response += f"\n🛡️: {defense}%"
    response += f"    🪄: {magic}%"
    response += f"\n👟: {agility}%"
    response += f"     💔: {healing}%"
    response += f"\n\n💵: {round(args[0].bal, 2)}"
    response += f"\n🔨: {args[0].gathering}"
    return response
