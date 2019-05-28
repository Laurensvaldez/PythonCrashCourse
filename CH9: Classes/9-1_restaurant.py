# Make a a class called Restaurant
class Restaurant:
    """A simple restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant is called " + self.restaurant_name + ".")
        print("And the cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " is open.")



all_you_can_eat = Restaurant("sumo", "sushi")
all_you_can_eat.describe_restaurant()
all_you_can_eat.open_restaurant()
print("------------------------------------")
a_la_carte = Restaurant("Aqua Asia", "sushi")
a_la_carte.describe_restaurant()
a_la_carte.open_restaurant()

