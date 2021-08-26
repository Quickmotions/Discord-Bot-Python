from Commands.update_csv import start_update_csv


def give_xp(xp_amount, skill_name, user_data, all_user_data):
    # unpack users data for specified skill
    level, current_xp, next_level_xp = user_data.skills[skill_name]
    current_xp = xp_amount + current_xp

    # loop leveling up until you dont have enough xp to level up
    if next_level_xp != "Max Level":
        while current_xp >= next_level_xp:
            current_xp -= next_level_xp
            level += 1
            if level < 50:
                next_level_xp = round(next_level_xp * (1.2 - (0.004 * level)))
            else:
                next_level_xp = "Max Level"
                break


    user_data.skills[skill_name] = [level, current_xp, next_level_xp]

    from Commands.update_csv import start_update_csv
    start_update_csv(all_user_data)


def setup_skills(user, users):
    if 'Combat' not in user.skills:
        user.skills['Combat'] = [0, 0, 100]
    if 'Magic' not in user.skills:
        user.skills['Magic'] = [0, 0, 100]
    if 'Agility' not in user.skills:
        user.skills['Agility'] = [0, 0, 100]
    if 'Healing' not in user.skills:
        user.skills['Healing'] = [0, 0, 100]
    if 'Defense' not in user.skills:
        user.skills['Defense'] = [0, 0, 100]
    if 'Stealing' not in user.skills:
        user.skills['Stealing'] = [0, 0, 100]
    if 'Luck' not in user.skills:
        user.skills['Luck'] = [0, 0, 100]
    if 'Fishing' not in user.skills:
        user.skills['Fishing'] = [0, 0, 100]
    if 'Mining' not in user.skills:
        user.skills['Mining'] = [0, 0, 100]
    if 'Woodcut' not in user.skills:
        user.skills['Woodcut'] = [0, 0, 100]
    if 'Health' not in user.skills:
        user.skills['Health'] = [0, 0, 100]

    start_update_csv(users)


