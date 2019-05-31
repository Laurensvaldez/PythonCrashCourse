# Add an attribute called login_attempts to your User class from Exercise 9-3
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
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Increment the value of login by 1."""
        self.login_attempts += 1


    # Write another method called reset_login_attempts() that resets the value of login_attempts to 0
    def reset_login_attempts(self):
        self.login_attempts = 0

# Make an instance of the User class and call increment_login_attempts() several times, and call reset_login_attempts()
laurens = User("Laurens", "Salcedo Valdez", 29, "Rotterdam", "in a relationship")
laurens.describe_user()
laurens.greet_user()

laurens.increment_login_attempts()
print("Login attempts are: " + str(laurens.login_attempts))

laurens.increment_login_attempts()
print("Login attempts are: " + str(laurens.login_attempts))

laurens.increment_login_attempts()
print("Login attempts are: " + str(laurens.login_attempts))

laurens.increment_login_attempts()
print("Login attempts are: " + str(laurens.login_attempts))

laurens.reset_login_attempts()
print("Login attempts are reset to: " + str(laurens.login_attempts))

# Print login_attempts again to make sure it was reset to 0
print("Login attempts are reset to: " + str(laurens.login_attempts))
