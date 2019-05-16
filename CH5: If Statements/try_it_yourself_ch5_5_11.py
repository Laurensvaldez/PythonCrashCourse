# Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2 & 3
# Store numbers 1 through 9 in a list
# loop through the list
# Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output


numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print ("1st")
    elif number == 2:
        print ("2nd")
    elif number == 3:
        print ("3rd")
    else:
        print (str(number) + "th")