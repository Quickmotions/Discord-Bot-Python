def hunt_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        if args[3][0] == "list":
            return ["multiple",
                    "All hunting Locations:",
                    "Plains: (easy)",
                    "Swamp: (medium)",
                    "Mountains: (hard)",
                    "Volcano: (pog)"]
    else:
        return "Incorrect argument, \nMust be: list or (location)"
