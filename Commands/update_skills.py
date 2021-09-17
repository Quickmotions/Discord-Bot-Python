from Commands.update_csv import start_update_csv
from Commands.stats_command import stats_c

skill_info = {
    'Combat': '4% Combat Damage, 4% Health Increase, 4% Shield Increase',
    'Magic': '+10% Magic Damage',
    'Agility': '6% Agility Damage,  0.2% Dodge,',
    'Healing': '7% Healing Increase, 3% Health Increase',
    'Defense': '+8% Shield Increase, 2% Health Increase, 0.25% Dodge Decrease',
    'Critical': '+0.25% Critical Chance',
    'Health': '+6% Health',
    'Stealing': '+1% Stealing Chance',
    'Luck': '+1% Gambling Chance',
    'Dodge': '+0.5% dodge, 5% Shield Decrease'
}



def give_xp(xp_amount, skill_name, user_data, all_user_data):
    # unpack users data for specified skill

    # loop leveling up until you dont have enough xp to level up
    if skill_name == "Player":
        level, current_xp, next_level_xp, skill_points = user_data.skills[skill_name]
        current_xp = xp_amount + current_xp
        if next_level_xp != "Max Level":
            while current_xp >= next_level_xp:
                current_xp -= next_level_xp
                level += 1
                skill_points += 1
                if level < 200:
                    # next_level_xp = round(next_level_xp * (1.1 - (0.0003 * level)))
                    next_level_xp = round(next_level_xp + 30)
                else:
                    next_level_xp = "Max Level"
                    break

        user_data.skills[skill_name] = [level, current_xp, next_level_xp, skill_points]
    else:
        level, current_xp, next_level_xp = user_data.skills[skill_name]
        current_xp = xp_amount + current_xp
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

    start_update_csv(all_user_data)


def skills_c(*args):
    skills = args[0].skills
    skill_points = skills["Player"][3]
    if len(args[3]) > 0:
        user_input = args[3][0].title()
        if user_input in skills:
            if user_input not in ['Fishing', 'Mining', 'Woodcut']:
                skill_name = user_input
                if len(args[3]) > 1:

                    try:
                        increase = int(args[3][1])
                        if increase > skill_points:
                            return f"You only have {skill_points} left."
                        if skills[skill_name] == 50:
                            return f"{skill_name} is already at max level."
                        if skills[skill_name] + increase > 50:
                            increase = 50 - skills[skill_name]
                        skills[skill_name] += increase
                        args[0].skills["Player"][3] -= increase
                        skill_points -= increase
                        start_update_csv(args[2])
                        return f"Put {increase} skillpoints into {skill_name}. You have {skill_points} left."
                    except Exception as e:
                        return e
                else:
                    return f"{skill_name} : {skill_info[skill_name]}"
            else:
                return f"Cannot put skillpoints into gathering skills."
        elif user_input.lower() == "reset":
            if 'ResetSigil' in args[0].inv:
                if args[0].inv['ResetSigil'] > 0:
                    args[0].inv['ResetSigil'] -= 1
                    args[0].skills["Player"][3] = args[0].skills["Player"][0]  # set skill point amount to total level
                    args[0].skills['Combat'] = 0
                    args[0].skills['Magic'] = 0
                    args[0].skills['Agility'] = 0
                    args[0].skills['Healing'] = 0
                    args[0].skills['Defense'] = 0
                    args[0].skills['Stealing'] = 0
                    args[0].skills['Luck'] = 0
                    args[0].skills['Critical'] = 0
                    args[0].skills['Health'] = 0
                    args[0].skills['Dodge'] = 0
                    start_update_csv(args[2])
                    return f"Reset all skill level and gave you {args[0].skills['Player'][0]} skillpoints.\n" \
                           f"Costing you 1 ResetSigil you have {args[0].inv['ResetSigil']}(s) left."
                else:
                    return "You do not own any ResetSigils"
            else:
                return "You do not own any ResetSigils"

        elif user_input.lower() == "help":
            return "'stats (skill name) (number)' - adds skillpoints\n" \
                   "'stats reset' - reset skill points\n" \
                   "'stats (skill name) - view info about skill"
        else:
            return f"Incorrect use of command:\nTry 'stats (skill name) (number)' to add skillpoints or " \
                   f"'stats reset' to reset skill points"
    else:
        return stats_c(args[0])


def setup_skills(user, users):
    if 'Player' not in user.skills:
        user.skills['Player'] = [0, 0, 100, 0]
    if 'Combat' not in user.skills:
        user.skills['Combat'] = 0
    if 'Magic' not in user.skills:
        user.skills['Magic'] = 0
    if 'Agility' not in user.skills:
        user.skills['Agility'] = 0
    if 'Healing' not in user.skills:
        user.skills['Healing'] = 0
    if 'Defense' not in user.skills:
        user.skills['Defense'] = 0
    if 'Stealing' not in user.skills:
        user.skills['Stealing'] = 0
    if 'Luck' not in user.skills:
        user.skills['Luck'] = 0
    if 'Critical' not in user.skills:
        user.skills['Critical'] = 0
    if 'Health' not in user.skills:
        user.skills['Health'] = 0
    if 'Dodge' not in user.skills:
        user.skills['Dodge'] = 0
    if 'Fishing' not in user.skills:
        user.skills['Fishing'] = [0, 0, 100]
    if 'Mining' not in user.skills:
        user.skills['Mining'] = [0, 0, 100]
    if 'Woodcut' not in user.skills:
        user.skills['Woodcut'] = [0, 0, 100]

    start_update_csv(users)
