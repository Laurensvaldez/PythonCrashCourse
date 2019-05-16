# start with your program from Exercise 4-1
# make a copy of the list of pizzas, and call it friend_pizzas

pizza_list = ["Pepperoni", "Margaritha", "BBQ"]

friend_pizzas = pizza_list[:]

pizza_list.append("Vegetarian")

friend_pizzas.append("Calzone")

print ("My favorite pizzas are:\n ")
for pizzas in pizza_list:
    print (pizzas)

print("\n")

print("My friend's favorite pizzas are:\n ")
for pizzas in friend_pizzas:
    print(pizzas)