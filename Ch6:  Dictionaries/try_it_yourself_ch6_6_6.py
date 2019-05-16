favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

list_names = ['jen', 'laurens', 'sarah', 'edward', 'phil', 'elba', 'fran']

# Make a list of people who should take the favorite language poll. Include some names that are already in the
# dictionary and some that are not.
# Loop through the list of people who should take the poll. If they have already taken the poll, print a message
# thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.

for people in list_names:
    if people not in favorite_languages:
        print(people.title() + " could you take the poll?")
    else:
        print(people.title() + " thank you for taking the poll!")