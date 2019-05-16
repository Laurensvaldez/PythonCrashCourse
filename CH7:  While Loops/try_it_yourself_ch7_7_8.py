sandwich_orders = ['ham kaas', 'gehakt', 'lettuce', 'plain']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()

    print("I made your " + order + " sandwich.")
    finished_sandwiches.append(order)