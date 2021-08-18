def give_xp(xp_amount, skill_name, user_data, all_user_data):
    # unpack users data for specified skill
    level, current_xp, next_level_xp = user_data.skills[skill_name]
    current_xp = xp_amount
    # loop leveling up until you dont have enough xp to level up
    while current_xp >= next_level_xp:
        current_xp -= next_level_xp
        level += 1
        next_level_xp = round(next_level_xp * 1.2)

    user_data.skills[skill_name] = [level, current_xp, next_level_xp]

    from Commands.update_csv import start_update_csv
    start_update_csv(all_user_data)
