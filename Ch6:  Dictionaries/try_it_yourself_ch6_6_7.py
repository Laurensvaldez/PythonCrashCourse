# Start with the program you wrote for Exercise 6-1 (page 102)
# Make two dictionaries representing different people, and store all three dictionaries in a list called people.
# Loop through your list of people. As you loop through the list, print everything you know about each person.

# First make an empty list to store the people in it
people = []

# Second, create three dictionaries of people and store information in it
person = {
    'first_name': 'elba',
    'last_name': 'lopez',
    'age': 23,
    'city': 'rotterdam',
}
people.append(person)

person = {
    'first_name': 'laurens',
    'last_name': 'salcedo valdez',
    'age': 29,
    'city': 'Rotterdam',
}
people.append(person)

person = {
    'first_name': 'jonathan',
    'last_name': 'diaz moreno',
    'age': 21,
    'city': 'Rotterdam',
}
people.append(person)

# Third, loop through your list of people
for person in people:
    name = person["first_name"].title() + " " + person["last_name"].title()
    age = str(person["age"])
    location = person["city"].title()

    print(name + " of " + location + " is " + age + " old.")