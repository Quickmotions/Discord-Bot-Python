from Commands.update_csv import start_update_csv
from Commands.item_command import item_list


guild_list = {
    'Leather': 10,
    'WaterRune': 20,
    'Bone': 20,
    'Paper': 35,
    'IceRune': 150,
    'SandRune': 250,
    'GunPart': 300,
    'EarthRune': 500,
    'FireRune': 2000,
    'BlackLeather': 70,
    'ShadeWoodLog': 45,
    'Diamond': 50,
    'Ruby': 50,
    'Sapphire': 50,
    'RemovalSigil': 2000,
    'TrainingPoint': 20,
    'HunterRing': 2500,
    'SorcererWand': 5000,
    'MagicDagger': 5000,
    'AssassinsHelmet': 1000,
    'AssassinsChestplate': 1000,
    'AssassinsLeggings': 1000,
    'AssassinsBoots': 1000,
    'Assassinate': 1400,
    'SkyShard': 900,
    'Stab': 400,
    'ShadowSlice': 500,
    'ShadowBeam': 2000,
    'ShadowStep': 420,
    'DarkCharge': 1750,
    'Shatter': 2400,
    'RagingFury': 1950,
    'TormentShard': 3100,


}



def guild_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        if len(args[3]) > 1:
            if args[3][0] == "buy":
                for item in guild_list:
                    if item.lower() == args[3][1].lower():
                        amount = 1
                        if len(args[3]) > 2:
                            amount = int(args[3][2])
                            
                        if args[0].inv['HuntPoint'] >= guild_list[item] * amount:
                            args[0].inv['HuntPoint'] -= guild_list[item] * amount

                            # test if item being bought is a card and add it to card menu instead of inv
                            for card in item_list:
                                if item in card[0].keys():
                                    if card[1] == 'Card':
                                        if item not in args[0].cards:
                                            args[0].cards[item] = 0
                                        args[0].cards[item] += amount
                                        start_update_csv(args[2])
                                        return f"Bought {amount} {item} for {guild_list[item] * amount} HuntPoints"

                            if item not in args[0].inv:
                                args[0].inv[item] = 0
                            args[0].inv[item] += amount
                            start_update_csv(args[2])
                            
                            return f"Bought {amount} {item} for {guild_list[item] * amount} HuntPoints"
                        else:
                            return f"You dont own enough HuntPoints:\nItem - {amount} {item} costs {guild_list[item] * amount} HuntPoints"
            else:
                return "To buy an item from the guild shop:\nUse 'guild buy (item) (amount)'"
        else:
            return "To buy an item from the guild shop:\nUse 'guild buy (item) (amount)'"

    else:
        shop_menu = "Hunt Guild Shop:\n\n"
        for item in guild_list:
            shop_menu += f"{item.title()} : {guild_list[item]} HuntPoints\n"
        shop_menu += "Type: 'guild buy (item) (amount)' to buy it:"
        return shop_menu
