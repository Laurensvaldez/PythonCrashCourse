# do the following to create a program that simulates how websites ensure that everyone has a unique username

current_users = ['laurens', 'rensley', 'jeremy', 'ian', 'ergin']
new_users = ['jonathan', 'khristian', 'domingo', 'ian', 'ergin']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print ("The username "+ new_user + " is already in use, please choose another one.")
    else:
        print ("The username " + new_user + " is available.")