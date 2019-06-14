# Write a separate Privileges class
# The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7
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
        # Initialize an empty set of privileges.
        self.privileges = Privileges()

    # Write a method called show_privileges() that lists the administrator's set of privileges.


class Privileges:
    """A class to store and Admin's privileges."""
    def __init__(self, privileges=[]):
        """Stores a list of privileges."""
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")

# Make a Privileges instance as an attribute in the Admin class.
eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges.show_privileges()

print("\nAdding privileges...")
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()
# Create a new instance of Admin and use your method to show its privileges.