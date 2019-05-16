sandwich_orders = ['ham kaas', 'gehakt', 'lettuce', 'plain', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("-------------------")

while sandwich_orders:
    order = sandwich_orders.pop()

    print("I made your " + order + " sandwich.")
    finished_sandwiches.append(order)
