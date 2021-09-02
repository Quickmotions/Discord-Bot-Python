from Commands.item_command import item_list


def use_card(card, user, event):
    combat_base = user.skills['Combat'] + user.equipment_stats['Combat']
    defense_base = user.skills['Defense'] + user.equipment_stats['Defense']
    magic_base = user.skills['Magic'] + user.equipment_stats['Magic']
    agility_base = user.skills['Agility'] + user.equipment_stats['Agility']
    healing_base = user.skills['Healing'] + user.equipment_stats['Healing']
    health_base = user.skills['Health'] + user.equipment_stats['Health']

    combat = (((4 * combat_base) - (2 * defense_base) - (1 * healing_base)) / 100) + 1
    defense = (((10 * defense_base) - (4 * health_base)) / 100) + 1
    magic = (((10 * magic_base) - (2 * defense_base) - (1 * healing_base)) / 100) + 1
    agility = (((6 * agility_base) - (2 * defense_base) - (1 * healing_base)) / 100) + 1
    healing = (((10 * healing_base) - (2 * combat_base) - (2 * agility_base) - (2 * magic_base)) / 100) + 1

    if combat < 0.01:
        combat = 0.01
    if defense < 0.01:
        defense = 0.01
    if magic < 0.01:
        magic = 0.01
    if agility < 0.01:
        agility = 0.01
    if healing < 0.01:
        healing = 0.01

    damage_dealt = 0
    shield_gained = 0
    heal_gained = 0
    extra_draw = False
    for card_chosen in item_list:
        if card_chosen[1] == 'Card':  # filter cards only
            if card in card_chosen[0].keys():
                for skill, amount in card_chosen[2].items():
                    if skill == "Combat":
                        damage_dealt += round(amount * combat)

                    elif skill == "Defense":
                        shield_gained += round(amount * defense)

                    elif skill == "Magic":
                        damage_dealt += round(amount * magic)

                    elif skill == "Agility":
                        damage_dealt += round(amount * agility)

                    elif skill == "Healing":
                        heal_gained += round(amount * healing)

                    elif skill == "Self":
                        event.hp -= amount

                    elif skill == "Draw":
                        extra_draw = True

                    elif skill == "Finisher":
                        if event.mob_hp / event.mob_max_hp <= 0.2:
                            damage_dealt += round(amount * agility)

                    elif skill == "Destroy":
                        if user.cards[card] > 1:
                            user.cards[card] -= 1
                        else:
                            del user.cards[card]

    if user.equipment['Hand'] == "Shield":
        shield_gained += round(3 * defense)

    event.mob_hp -= damage_dealt
    event.shield += shield_gained
    return [damage_dealt, shield_gained, extra_draw, heal_gained]
