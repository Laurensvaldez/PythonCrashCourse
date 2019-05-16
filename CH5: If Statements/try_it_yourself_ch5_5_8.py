# Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a
# greeting to each user after the log in to a website. Loop through the list, and print a greeting to each user:

# if the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# otherwise, print a genering greeting, such as hello Eric, thank you for logging in again.

usernames = ['admin', 'jimisthebest', 'rstarke', 'zerosavagery', 'blokje94']

for names in usernames:
    if names == 'admin':
        print ("Hello " + names.title() + ", would you like to see a status report?\n" )
    else:
        print ("Hello " + names.title() + ", thank you for logging in.\n")
