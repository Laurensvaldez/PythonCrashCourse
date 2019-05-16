# make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

multiples_three = list(range(3,31))
lijst_gebruikt = []

for numeros in multiples_three:
    numero= numeros * 3
    lijst_gebruikt.append(numero)

print(lijst_gebruikt)