# work with lists
# to work in range

squares = []
for value in range (1,11):
    square = value**2
    squares.append(square)

print (squares)

# you can also use the min, max and sum functions to find a certain value in a list
# min will find you the lowest number in the list, for example:
# digits = [1, 2, 3, 4, 5, 6]
# min(digits) >>> 1
# max(digits) >>> 6
# sum(digits) >>> 21 -> this will add all the numbers in the list

# list comprehensions
squares = [ value**2 for value in range(1,11)]
print (squares)
# the list comprehension generates the same result as the code above