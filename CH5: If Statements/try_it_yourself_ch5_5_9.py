available_usernames = []

if available_usernames:
    for username in available_usernames:
        if username == 'admin':
            print ("Hello admin, would you like to see a status report?")
        else:
            print ("Hello " + username + ", thank you for logging in again!")
else:
    print ("We need to find some users!")