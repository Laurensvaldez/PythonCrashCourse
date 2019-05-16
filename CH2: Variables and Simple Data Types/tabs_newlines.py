print ("Python")

# adding \t will give you a tab on the print function
print ("\tPython")
# adding the \n will give you a new line on the print function
print("Languages:\nPython\nC\nJavaScript")

# you can also combine the tab and newline characters

# to ensure that there is no unnecessary whitespace, you can use the rstrip() method

# example:

favorite_language = 'python '
print (favorite_language)
print (favorite_language.rstrip())
# in this case the whitespace is removed temporarily

# rstrip is for the right side
# lstrip is for the left side
# strip is for both side
# these are most commonly used for cleaning up input from users