# In this file we will import the function of pizza_import.py
import pizza_import
print("Importing all the functions in the module")
pizza_import.make_pizza(16, 'pepperoni')
pizza_import.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print("-------------------------------------------")
# To use the import the following syntax is necessary:
# module_name.function_name()

# You can also import a specific function from a module. Here's the general syntax for this approach:
# from module_name import function_name

# You can import as many functions as you want from a module by seperating each function's name with a comma:
# from module_name import function_0, function_1, function_2

# Using 'as' to Give a Function an Alias
# Here we give the function make_pizza() an alias, mp(), by importing make_pizza as mp. The 'as' keyword renames a
# function using the alias you provide.

from pizza_import import make_pizza as mp
print("Importing specific function under an alias")
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# The general syntax for providing an alias is:
# from module_name import function_name as fn
print("-------------------------------------------")
# You can also provide an alias for a module name.
# Such as:
import pizza_import as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# The general syntax for providing an alias for a module is:
# import module_name as mn
print("-------------------------------------------")

# You can tell Python to import every function in a module by using the asterisk (*) operator
# Example:
from pizza_import import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# The general syntax for providing this import is:
# from module_name import *