# keyword arguments
print("Keyword arguments:")
def make_shirt(size= 'large', message= 'I love Python'):
    print("The size of the t-shirt is: " + size + " and the message on it is: " + "'" + message + "'.")

make_shirt()
make_shirt(size= "medium")
make_shirt(size= "XXL", message= "I just started learning Python")