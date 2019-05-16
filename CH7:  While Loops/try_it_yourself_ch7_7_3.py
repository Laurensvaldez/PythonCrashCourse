# Multiples of Ten
# Ask the user for a number, and then report whether the number is a multiple of 10 or not.

math_number = input("Please provide me of a number, so I can report if it's a multiple of 10. ")
math_number = int(math_number)

if math_number % 10 == 0:
    print(True)
else:
    print(False)