# T-shirt
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt

# positional arguments
print("Positional arguments:")
def make_shirt(size, message):
    print("The size of the t-shirt is: " + size + " and the message on it is: " + "'" + message + "'.")

make_shirt('large', 'I am Groot!')

# keyword arguments
print("Keyword arguments:")
def make_shirt(size= 'large', message= 'I am Groot!'):
    print("The size of the t-shirt is: " + size + " and the message on it is: " + "'" + message + "'.")

make_shirt()