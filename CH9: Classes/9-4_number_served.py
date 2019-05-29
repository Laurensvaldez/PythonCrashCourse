# Start with your program from Exercise 9-1
class Restaurant:
    """A simple restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        # Add an attribute called number_served with a default value of 0
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant is called " + self.restaurant_name + ".")
        print("And the cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " is open.")

    def customers_served(self):
        print("The restaurant has served " + str(self.number_served) + " people.")

    def set_number_served(self, served_update):
        """Add a method called set_number_served() that lets you set the number of customers that have been served"""
        self.number_served = served_update

    def increment_number_served(self, increment_served):
        """Method lets you increment the number of customers who's been served."""
        self.number_served += increment_served

# Create an instance called restaurant from this class
restaurant = Restaurant('vapiano', 'mix')

# Print the number of customers the restaurant has served, and then change this value to print it again
restaurant.customers_served()
# And then change this value to print it again
restaurant.number_served = 4
restaurant.customers_served()


# Add a method called set_number_served() that lets you set the number of customers that have been served
# (Done)

# Call this method with a new number and print the value again
restaurant.set_number_served(6)
restaurant.customers_served()

# Add a method called increment_number_served() that lets you increment the number of customers who's been served.
# Done
restaurant.increment_number_served(20)
restaurant.customers_served()

# Call this method with any number you like that could represent how many customers were served in, say, a business day
