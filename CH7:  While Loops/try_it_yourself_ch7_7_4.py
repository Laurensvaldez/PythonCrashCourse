# Pizza toppings

# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
# As they enter each topping, print a message saying you'll add that topping to their pizza.

request_toppings = "What would you like on your pizza as toppings? You can add three toppings "
request_toppings += "\nEnter all the toppings you want and write 'finished' when you are done. > "

toppings = True
order = []
while toppings:
    request = input(request_toppings)

    if request == 'finished':
        toppings = False
        print("Your order for toppings is: ")
        for topping in order:
            print(topping.title())
        print("Thank you for your order and have a nice day! ")
    else:
        order.append(request)

