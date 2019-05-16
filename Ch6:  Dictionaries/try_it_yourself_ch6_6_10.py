# Favorite numbers

favorite_numbers = {
    "ian": [6, 7, 8],
    "elba": [7, 11, 12],
    "ergin": [8, 13, 14],
    "jonathan": [30, 31, 32],
    "tim": [19, 20, 21],
}

for person, numbers in favorite_numbers.items():
    print(person.title() + "'s favorite numbers are:")
    for number in numbers:
        print(number)