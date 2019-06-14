# Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 or Exercise 9-4
# Either version of the class will work; just pick the one you like better
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

class IceCreamStand(Restaurant):
    """An Ice Cream Stand, with a class of a restaurant."""
    # Add an attribute called flavors that stores a list of ice cream flavors
    def __init__(self, name, cuisine_type='ice_cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    # Write a method that displays these flavors
    def display_flavors(self):
        """Method that displays the flavors available."""
        for flavor in self.flavors:
            print("- " + flavor.title())

# Create an instance of IceCreamStand, and call this method


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.display_flavors()