def start_update_csv(users):
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join('..')))
    from users import update_csv
    update_csv(users)
