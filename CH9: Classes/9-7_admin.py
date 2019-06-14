# Write a class called Admin that inherits from the User class you wrote in Exercise 9-3
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

class Admin(User):
    """A class to describe the Admin."""
    def __init__(self, first_name, last_name, age, birthplace, relationship_status):
        super().__init__(first_name, last_name, age, birthplace, relationship_status)
        # Add an attribute, privileges, that stores a list of strings
        self.privileges = []

    # Write a method called show_privileges() that lists the administrator's set of priviliges.
    def show_privileges(self):
        print("The privileges of the administrator are: ")
        for privilege in self.privileges:
            print("- " + privilege)


super_user = Admin("laurens", "salcedo valdez", 29, "rotterdam", "in a relationship")
super_user.describe_user()
super_user.privileges = [
    'can reset password',
    'can delete users',
    'can grant access to users',
    'can suspend users',
]
super_user.show_privileges()