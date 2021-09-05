from Commands.update_csv import start_update_csv

def party_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        if args[3][0] == 'invite':
            if len(args[3]) > 1:
                for target in args[2]:
                    if str(args[3][1]) == f"<@!{target.user_id}>" or str(args[3][1]) == f"<@{target.user_id}>":
                        target.party.append([args[0].user_id, args[0].username, 'invite'])
                        start_update_csv(args[2])
                        return f"Invited {target.username} to your party:\nThey need to type `party join' to accept."

        elif args[3][0] == 'join':
            if len(args[0].party) > 2:
                for invite in args[0].party:
                    if invite[2] == 'invite':
                        party_invitee_user_id, party_leader, invite = invite
                        for user in args[2]:
                            if user.user_id != args[0].user_id:
                                for member in user.party:
                                    if member[0] == party_invitee_user_id:
                                        if [args[0].user_id, args[0].username, 'member'] not in user.party:
                                            user.party.append([args[0].user_id, args[0].username, 'member'])
                                        if [user.user_id, user.username, 'member'] not in args[0].party:
                                            args[0].party.append([user.user_id, user.username, 'member'])

                        has_invite = False
                        for member in args[0].party:

                            if member[2] == 'invite':
                                args[0].party.remove(member)
                                has_invite = True

                        start_update_csv(args[2])
                        if has_invite:
                            return f"You joined {party_leader}s Party"
                        else:
                            return f"You have no party invites"
            else:
                return "You're already in a party, type 'party quit'"


        elif args[3][0] == 'list':
            response_string = "Party List:"
            for member in args[0].party:
                if member[2] == 'member':
                    response_string += f"\n -{member[1]}"
            return response_string

        elif args[3][0] == 'quit' or args[3][0] == 'leave':
            for _ in args[0].party[1:]:
                for user in args[2]:
                    for member_to_remove in user.party:
                        if member_to_remove[0] == args[0].user_id:
                            user.party.remove(member_to_remove)
            args[0].party = [[args[0].user_id, args[0].username, 'member']]
            start_update_csv(args[2])
            return f"You left your current party."