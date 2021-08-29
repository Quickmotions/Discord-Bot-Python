card_list = {
    'slash':  "(combat) Damage - 3",  # 67
    'defend': "Shield - 5",  # 64
    'charge': "(agility) Damage - 2\nBonus - Extra Card Draw",  # 235
    'recharge': "Heal - 8",  # 75
    'punch': "(agility) Damage - 4",  # 125
    'shieldbash': "(combat) Damage - 2\nShield - 4",  # 141
    'bash': "(combat) Damage - 5",  # 124
    'slice': "(agility) Damage - 4\nHeal - 4",  # 100
    'snipe': "(magic) Damage - 7",  # 214
    'trickshot': "(magic) Damage - 5\nShield - 3",  # 150
    'whirlwind': "(magic) Damage - 5\nBonus - Extra Card Draw",  # 520
    'bomb': "(agility) Damage - 30\nBonus - Gets permanently destroyed",
    'towershield': "Shield - 12",  # 350
    'regeneration': "Heal - 25",  # 375
    'onepunch': "(combat) Damage - 30",  # 3333
    'slam': "(combat) Damage - 5\nShield - 5\nHeal - 4 ",  # 392
    'incinerate': "(magic) Damage - 11",  # 436
    'devastate': "(magic) Damage - 8\nShield - 2",  # 320
    'bite': "(agility) Damage - 10",  # 360
    'venom': "(magic) Damage - 3\nShield - 8",  # 390
    'smash': "(combat) Damage - 3\nHeal - 10",  # 281
}




def card_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        for card in card_list:
            if args[3][0] == card.lower():
                return f"Info for {args[3][0]} card:\n{card_list[args[3][0]]}"
    else:
        return f"Incorrect use of card:\ntry 'card (card-name)'"


def use_card(card, user, event):
    combat = 1 + (0.1 * (user.skills['Combat'][0] + user.equipment_stats['Combat']))
    defense = 1 + (0.1 * (user.skills['Defense'][0] + user.equipment_stats['Defense']))
    magic = 1 + (0.1 * (user.skills['Magic'][0] + user.equipment_stats['Magic']))
    agility = 1 + (0.1 * (user.skills['Agility'][0] + user.equipment_stats['Agility']))
    healing = 1 + (0.1 * (user.skills['Healing'][0] + user.equipment_stats['Healing']))
    damage_dealt = 0
    shield_gained = 0
    heal_gained = 0
    extra_draw = False

    if card == "Slash":
        damage_dealt = round(3 * combat)
    if card == "Defend":
        shield_gained = round(5 * defense)
    if card == "Charge":
        damage_dealt = round(2 * agility)
        extra_draw = True
    if card == "Recharge":
        heal_gained = round(8 * healing)
    if card == "Punch":
        damage_dealt = round(4 * agility)
    if card == "Shieldbash":
        damage_dealt = round(2 * combat)
        shield_gained = round(4 * defense)
    if card == "Bash":
        damage_dealt = round(5 * combat)
    if card == "Slice":
        damage_dealt = round(4 * agility)
        heal_gained = round(4 * healing)
    if card == "Snipe":
        damage_dealt = round(7 * magic)
    if card == "Trickshot":
        damage_dealt = round(5 * magic)
        shield_gained = round(3 * defense)
    if card == "Whirlwind":
        damage_dealt = round(5 * magic)
        extra_draw = True
    if card == "Bomb":
        if user.cards['Bomb'] > 1:
            user.cards['Bomb'] -= 1
        else:
            del user.cards['Bomb']
        damage_dealt = round(30 * agility)
    if card == "Towershield":
        shield_gained = round(12 * defense)
    if card == "Regeneration":
        heal_gained = round(25 * healing)
    if card == "Onepunch":
        damage_dealt = round(30 * combat)
    if card == "Slam":
        damage_dealt = round(5 * combat)
        shield_gained = round(5 * defense)
        heal_gained = round(4 * healing)
    if card == "Incinerate":
        damage_dealt = round(11 * magic)
    if card == "Devastate":
        damage_dealt = round(8 * magic)
        shield_gained = round(2 * defense)
    if card == "Bite":
        damage_dealt = round(10 * agility)
    if card == "Venom":
        damage_dealt = round(3 * magic)

    if card == "Smash":
        damage_dealt = round(3 * combat)
        heal_gained = round(10 * healing)

    if user.equipment['Hand'] == "Shield":
        shield_gained += round(3 * defense)

    event.mob_hp -= damage_dealt
    event.shield += shield_gained
    return [damage_dealt, shield_gained, extra_draw, heal_gained]
