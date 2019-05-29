# Start with your class from exercise 9-1. Create three different instances from the class, and call
# describe_restaurant() for each instance

class Restaurant:
    """A simple restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg_name = "The restaurant is called " + self.restaurant_name + "."
        msg_type = "And the cuisine type is " + self.cuisine_type + "."
        print("\n" + msg_name)
        print(msg_type)

    def open_restaurant(self):
        msg_open = "The restaurant " + self.restaurant_name.title() + " is open."
        print("\n" + msg_open)

cheap = Restaurant("vapiano", "mix")
cheap.describe_restaurant()

mid_range = Restaurant("sumo", "sushi")
mid_range.describe_restaurant()

expensive = Restaurant("aqua asia", "sushi")
expensive.describe_restaurant()

