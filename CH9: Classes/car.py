class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # See how you can add an attribute without putting it above after the __init__
        # This means that it's not necessary to write an argument when creating an instance
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    # Modifying an Attribute's value through a method
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        # Incrementing an Attribute's value through a method.
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# You can also modify an Attribute value directly:
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Regarding the update_odometer method
my_new_car.update_odometer(24)
my_new_car.read_odometer()

# Let's add a little bit of logic to make sure no one tries to roll back the odometer reading:
# See Update_odometer with the if-statement

# Incrementing an Attribute's value through a method (2).
my_used_car = Car('subaru', 'outback', '2013')
print(my_used_car.get_descriptive_name())

# Pointing out the current odometer stand
my_used_car.update_odometer(23500)
my_used_car.read_odometer()

# incrementing a value through a method
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
