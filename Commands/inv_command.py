from Commands.update_csv import start_update_csv

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
        for helmet in helmets:
            if helmet.lower() == user_input and helmet in args[0].inv:
                previous = args[0].equipment['Head']
                args[0].equipment['Head'] = helmet
                response = update_and_return(args[2], previous, helmet, 'Head')

        for chestplate in chestplates:
            if chestplate.lower() == user_input and chestplate in args[0].inv:
                previous = args[0].equipment['Chest']
                args[0].equipment['Chest'] = chestplate
                response = update_and_return(args[2], previous, chestplate, 'Chest')

        for legging in leggings:
            if legging.lower() == user_input and legging in args[0].inv:
                previous = args[0].equipment['Legs']
                args[0].equipment['Legs'] = legging
                response = update_and_return(args[2], previous, legging, 'Legs')

        for boot in boots:
            if boot.lower() == user_input and boot in args[0].inv:
                previous = args[0].equipment['Feet']
                args[0].equipment['Feet'] = boot
                response = update_and_return(args[2], previous, boot, 'Feet')

        for hand in hands:
            if hand.lower() == user_input and hand in args[0].inv:
                previous = args[0].equipment['Hand']
                args[0].equipment['Hand'] = hand
                response = update_and_return(args[2], previous, hand, 'Hand')

        for finger in fingers:
            if finger.lower() == user_input and finger in args[0].inv:
                previous = args[0].equipment['Ring']
                args[0].equipment['Ring'] = finger
                response = update_and_return(args[2], previous, finger, 'Ring')
        set_equipment_stats(args[0], args[2])
        return response
    else:
        return "Incorrect use of equip command:\nTry 'equip (itemname)'"


def update_and_return(user_data, previous, item, slot):
    start_update_csv(user_data)

    return f"Replaced {previous} with {item} in {slot} Slot."


# equipment has been split into a list of 2 dictioinarys, use first to store equipment, and use second to store the
# temp stats gained. need to set up a rule to split these in the users class


def sort_inventory(inv):
    # categories: special, resource, else
    special = ['TrainingPoint', 'WorkPoint', 'HuntPoint', 'WaterRune', 'IceRune', 'SandRune', 'EarthRune', 'FireRune']
    resource = ['Coal', 'Cod', 'Mackerel', 'Carp', 'Trout', 'Salmon', 'Catfish', 'Tuna', 'Stone', 'Limestone',
                'Basalt', 'Ironore', 'Goldore', 'Tinore', 'Ruby', 'Sapphire', 'Diamond', 'OakLog', 'SpruceLog',
                'PineLog', 'BeechLog', 'MapleLog', 'AshLog', 'Leather', 'Bone', 'Paper', 'GunPart', 'IronIngot',
                'TinIngot', 'GoldIngot']

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


helmets = ['TinHelmet', 'ThiefHelmet', 'WarriorHelmet', 'FishHelmet', 'MinerHelmet']
chestplates = ['TinChestplate', 'ThiefChestplate', 'WarriorChestplate', 'FishChestplate', 'MinerChestplate']
leggings = ['TinLeggings', 'ThiefLeggings', 'WarriorLeggings', 'FishLeggings', 'MinerLeggings']
boots = ['TinBoots', 'ThiefBoots', 'WarriorBoots', 'FishBoots', 'MinerBoots']
hands = ['IronSword', 'MagicStaff', 'GemFishingRod', 'LuckyStick', 'BonerSword']
fingers = []


def set_equipment_stats(user, users):
    temp_stats = {'Combat': 0, 'Magic': 0, 'Agility': 0, 'Healing': 0, 'Defense': 0, 'Stealing': 0, 'Strength': 0, 'Healing': 0, 'Luck': 0, 'Fishing': 0, 'Mining': 0, 'Woodcut': 0, 'Health': 0}
    if user.equipment['Head'] == 'TinHelmet':
        temp_stats['Defense'] += 2
    if user.equipment['Head'] == 'ThiefHelmet':
        temp_stats['Stealing'] += 2
        temp_stats['Agility'] += 2
    if user.equipment['Head'] == 'WarriorHelmet':
        temp_stats['Combat'] += 2
    if user.equipment['Head'] == 'FishHelmet':
        temp_stats['Fishing'] += 2
    if user.equipment['Head'] == 'MinerHelmet':
        temp_stats['Mining'] += 2

    if user.equipment['Chest'] == 'TinChestplate':
        temp_stats['Defense'] += 2
    if user.equipment['Chest'] == 'ThiefChestplate':
        temp_stats['Stealing'] += 2
        temp_stats['Agility'] += 2
    if user.equipment['Chest'] == 'WarriorChestplate':
        temp_stats['Combat'] += 2
    if user.equipment['Chest'] == 'FishChestplate':
        temp_stats['Fishing'] += 2
    if user.equipment['Chest'] == 'MinerChestplate':
        temp_stats['Mining'] += 2

    if user.equipment['Chest'] == '1WarBornChestplate':
        temp_stats['Combat'] += 2
    if user.equipment['Chest'] == '2WarBornChestplate':
        temp_stats['Combat'] += 5
    if user.equipment['Chest'] == '3WarBornChestplate':
        temp_stats['Combat'] += 10

    if user.equipment['Chest'] == '1MagicChestplate':
        temp_stats['Magic'] += 2
    if user.equipment['Chest'] == '2MagicChestplate':
        temp_stats['Magic'] += 5
    if user.equipment['Chest'] == '3MagicChestplate':
        temp_stats['Magic'] += 10

    if user.equipment['Legs'] == 'TinLeggings':
        temp_stats['Defense'] += 2
    if user.equipment['Legs'] == 'ThiefLeggings':
        temp_stats['Stealing'] += 2
        temp_stats['Agility'] += 2
    if user.equipment['Legs'] == 'WarriorLeggings':
        temp_stats['Combat'] += 2
    if user.equipment['Legs'] == 'FishLeggings':
        temp_stats['Fishing'] += 2
    if user.equipment['Legs'] == 'MinerLeggings':
        temp_stats['Mining'] += 2

    if user.equipment['Feet'] == 'TinBoots':
        temp_stats['Defense'] += 2
    if user.equipment['Feet'] == 'ThiefBoots':
        temp_stats['Stealing'] += 2
        temp_stats['Agility'] += 2
    if user.equipment['Feet'] == 'WarriorBoots':
        temp_stats['Combat'] += 2
    if user.equipment['Feet'] == 'FishBoots':
        temp_stats['Fishing'] += 2
    if user.equipment['Feet'] == 'MinerBoots':
        temp_stats['Mining'] += 2

    if user.equipment['Hand'] == 'IronSword':
        temp_stats['Combat'] += 4
    if user.equipment['Hand'] == 'MagicStaff':
        temp_stats['Magic'] += 4
    if user.equipment['Hand'] == 'GemFishingRod':
        temp_stats['Fishing'] += 5
    if user.equipment['Hand'] == 'LuckyStick':
        temp_stats['Luck'] += 5
    if user.equipment['Hand'] == 'BonerSword':
        temp_stats['Agility'] += 6
    user.equipment_stats = temp_stats
    start_update_csv(users)




