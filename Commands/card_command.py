from Commands.item_command import item_list


def use_card(card, user, event):
    combat = 1 + (0.1 * (user.skills['Combat'] + user.equipment_stats['Combat']))
    defense = 1 + (0.1 * (user.skills['Defense'] + user.equipment_stats['Defense']))
    magic = 1 + (0.1 * (user.skills['Magic'] + user.equipment_stats['Magic']))
    agility = 1 + (0.1 * (user.skills['Agility'] + user.equipment_stats['Agility']))
    healing = 1 + (0.1 * (user.skills['Healing'] + user.equipment_stats['Healing']))
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
