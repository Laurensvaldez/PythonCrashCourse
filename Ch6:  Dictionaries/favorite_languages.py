favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

# The keys() method is useful when you don't need to work with all of the values in a dictionary.
# Example:
print("_______________________________________________________________")
print("\nThe next print is for the keys only (name).")
for name in favorite_languages.keys():
    print(name.title())

print("_______________________________________________________________")
# We'll loop through the names in the dictionary as we did previously, but when the name matches one our friends, we'll
# display a message about their favorite language:
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("  Hi " + name.title() +
            ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

print("_______________________________________________________________")
# You can also use the keys() method to find out if a particular person was polled. This time, let's find out if Erin
# took the poll.
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
print("_______________________________________________________________")
# One way to return items in a certain order is to sort the keys as they're returned in the for loop.
# You can use the sorted() function to get a copy of the keys in order.
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("_______________________________________________________________")
# If you are primarily interested in the values that a dictionary contains, you can use the values() method to return
# a list of values without any keys.
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
print("_______________________________________________________________")
# The above code pulls all the values from the dictionary without checking for repeats. That might work fine with a
# small number of values, but in a poll with a large number of respondents, this would result in a very repetitive list.
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
