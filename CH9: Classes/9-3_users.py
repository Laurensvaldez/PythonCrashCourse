# Make a class called User

class User:
    """A class to describe a user"""

    # Create two attributes called first_name and last_name
    # and then create several other attributes that are typically stored in a user profile
    def __init__(self, first_name, last_name, age, birthplace, relationship_status):
        """Initialize the first name and last name"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.birthplace = birthplace.title()
        self.relationship_status = relationship_status

    def describe_user(self):
        """This method prints a summary of the user"""
        msg_1 = "The user's first name is " + self.first_name + " and his/her last name is " + \
              self.last_name
        msg_2 = self.first_name + " " + self.last_name + " age is " + str(self.age) + \
                " and lives in " + self.birthplace + "."
        msg_3 = self.first_name + " " + self.last_name + " is currently " + self.relationship_status + \
                "."
        print("\n" + msg_1)
        print(msg_2)
        print(msg_3)

    def greet_user(self):
        """This method provides a personalized greeting to the user."""
        # print a personalized greeting to the user
        greeting = "Hello " + self.first_name + ", I hope you have a wonderful day!"
        print(greeting)

user_1 = User("laurens", "salcedo valdez", 29, "rotterdam", "in a relationship")
user_1.describe_user()
user_1.greet_user()

user_2 = User("elba", "torranzo lopéz", 23, "ibiza", "in a relationship")
user_2.describe_user()
user_2.greet_user()

user_3 = User("jonathan", "diaz moreno", 21, "rotterdam", "in a relationship")
user_3.describe_user()
user_3.greet_user()

user_4 = User("ruth", "diaz moreno", 50, "santo domingo", "married")
user_4.describe_user()
user_4.greet_user()