card_list = {
    'slash':  "Damage - 3",
    'defend': "Shield - 5",
    'charge': "Damage - 2\nBonus - Extra Card Draw",
    'recharge': "Heal - 8",
    'punch': "Damage - 4",
    'shieldbash': "Damage - 2\nShield - 4",
    'bash': "Damage - 5",
    'slice': "Damage - 4\nHeal - 4",
    'snipe': "Damage - 7",
    'trickshot': "Damage - 5\nShield - 3",
    'whirlwind': "Damage - 5\nBonus - Extra Card Draw",
    'bomb': "Damage - 30\nBonus - Gets permanently destroyed",
    'towershield': "Shield - 15",
    'regeneration': "heal - 20",
    'onepunch': "Damage - 30",

}


def card_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        for card in card_list:
            if args[3][0] == card.lower():
                return f"Info for {args[3][0]} card:\n{card_list[args[3][0]]}"
    else:
        return f"Incorrect use of card:\ntry 'card (card-name)'"


def use_card(card, user, event):
    combat = 1 + (0.1 * user.skills['Combat'][0])
    defense = 1 + (0.1 * user.skills['Defense'][0])
    damage_dealt = 0
    shield_gained = 0
    heal_gained = 0
    extra_draw = False

    if card == "Slash":
        damage_dealt = round(3 * combat)
    if card == "Defend":
        shield_gained = round(5 * defense)
    if card == "Charge":
        damage_dealt = round(2 * combat)
        extra_draw = True
    if card == "Recharge":
        heal_gained = 8
    if card == "Punch":
        damage_dealt = round(4 * combat)
    if card == "Shieldbash":
        damage_dealt = round(2 * combat)
        shield_gained = round(4 * defense)
    if card == "Bash":
        damage_dealt = round(5 * combat)
    if card == "Slice":
        damage_dealt = round(4 * combat)
        heal_gained = 4
    if card == "Snipe":
        damage_dealt = round(7 * combat)
    if card == "Trickshot":
        damage_dealt = round(5 * combat)
        shield_gained = round(3 * defense)
    if card == "Whirlwind":
        damage_dealt = round(5 * combat)
        extra_draw = True
    if card == "Bomb":
        if user.cards['Bomb'] > 1:
            user.cards['Bomb'] -= 1
        else:
            del user.cards['Bomb']
        damage_dealt = round(30 * combat)
    if card == "Towershield":
        shield_gained = round(15 * defense)
    if card == "Regeneration":
        heal_gained = 20
    if card == "Onepunch":
        damage_dealt = round(30 * combat)



    event.mob_hp -= damage_dealt
    event.shield += shield_gained
    return [damage_dealt, shield_gained, extra_draw, heal_gained]
