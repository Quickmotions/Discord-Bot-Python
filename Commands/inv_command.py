from Commands.update_csv import start_update_csv
from Commands.item_command import item_list


def inv_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    players_inv = sort_inventory(args[0].inv)
    page = 0
    if len(args[3]) > 0:
        page = int(args[3][0]) - 1

    setup_equipment(args[0], args[2])

    if page < 3:
        response = f"{args[0].username}s Inventory ({page+1}):\n--------------------"
        for item, value in players_inv[page].items():
            if int(value) > 0:
                response += f"\n{item} : {value}"
    else:
        response = f"{args[0].username}s Deck ({page+1}):\n--------------------"
        for item, value in args[0].cards.items():
            if int(value) > 0:
                response += f"\n{item} : {value}"
    response2 = "page: 1 = special, 2 = resource, 3 = other, 4 = cards"

    equipment = f"{args[0].username}s Equipment:\n--------------------"
    for slot, equipped in args[0].equipment.items():
        equipment += f"\n{slot} : {equipped}"


    return ["multiple", equipment, response, response2]


def equip_c(*args):
    if len(args[3]) > 0:
        user_input = args[3][0].lower()
        response = f"Cannot equip {user_input}"
        for item, slot, stats in item_list:
            for item_name, desc in item.items():
                if item_name.lower() == user_input and item_name in args[0].inv:
                    previous = args[0].equipment[slot]
                    args[0].equipment[slot] = item_name
                    start_update_csv(args[2])
                    set_equipment_stats(args[0], args[2])
                    return f"Replaced {previous} with {item} in {slot} Slot."
        return response
    else:
        return "Incorrect use of equip command:\nTry 'equip (itemname)'"


def sort_inventory(inv):
    # categories: special, resource, else
    special = ['TrainingPoint', 'WorkPoint', 'HuntPoint', 'WaterRune', 'IceRune', 'SandRune', 'EarthRune', 'FireRune']
    resource = ['Coal', 'Cod', 'Mackerel', 'Carp', 'Trout', 'Salmon', 'Catfish', 'Tuna', 'Stone', 'Limestone',
                'Basalt', 'Ironore', 'Goldore', 'Tinore', 'Ruby', 'Sapphire', 'Diamond', 'OakLog', 'SpruceLog',
                'PineLog', 'BeechLog', 'MapleLog', 'AshLog', 'Leather', 'Bone', 'Paper', 'GunPart', 'IronIngot',
                'TinIngot', 'GoldIngot', 'GemIngot', 'FishIngot']

    sorted_inv = [{}, {}, {}]
    for item, amount in inv.items():
        if item in special:
            sorted_inv[0][item] = amount
        elif item in resource:
            sorted_inv[1][item] = amount
        else:
            sorted_inv[2][item] = amount

    return sorted_inv


def setup_equipment(user, users_data):
    if len(user.equipment) == 0:
        user.equipment['Head'] = "None"
        user.equipment['Chest'] = "None"
        user.equipment['Legs'] = "None"
        user.equipment['Feet'] = "None"
        user.equipment['Hand'] = "None"
        user.equipment['Ring'] = "None"

    start_update_csv(users_data)


def set_equipment_stats(user, users):
    temp_stats = {'Combat': 0, 'Magic': 0, 'Agility': 0, 'Healing': 0, 'Defense': 0, 'Stealing': 0, 'Strength': 0, 'Healing': 0, 'Luck': 0, 'Fishing': 0, 'Mining': 0, 'Woodcut': 0, 'Health': 0}
    for item, slot, stats in item_list:
        for equipment_slot, equipment in user.equipment.items():
            for item_name, desc in item.items():
                if equipment == item_name:
                    for stat, amount in stats.items():
                        temp_stats[stat] += amount
    user.equipment_stats = temp_stats
    start_update_csv(users)




