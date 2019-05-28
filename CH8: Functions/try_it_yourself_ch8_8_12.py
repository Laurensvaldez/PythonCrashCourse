# Sandwiches
def order_sandwiches(*orders):
    """Write a function that accepts a list of items a person wants."""

    # Write a function that accepts a list of items a person wants on a sandwich
    for order in orders:
        print("Your order will be a: " + order + " sandwich.")

order_sandwiches('ham & cheese', 'cheese', 'cheese & bacon')