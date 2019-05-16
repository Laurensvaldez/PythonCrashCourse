# Looping through all Key-Value Pairs

# The following dictionary would store one person's username, first name, and last name:
user_0= {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

# What if you wanted to see everything stored in this user's dictionary?
for key, value in user_0.items():
    print("\nKey: " + key.title())
    print("Value: " + value.title())

# You can choose any names you want for these two variables, for example:
# for k, v in user_0.items()