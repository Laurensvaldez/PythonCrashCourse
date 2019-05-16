# Clean up your code from the previous exercise: Try It Yourself 6-3
# Glossary

glossary = {
    "concatenate": "When you patch strings, integers or floats together.",
    "indexing": "When you request a certain value by determining the position.",
    "dictionary": "In this case a data structure system in which keys with their values are stored.",
    "list": "As a dictionary, but without the use of keys and only objects, string, integers are stored",
    "for-loop": "The use of a function that enables the user to use loops in codes.",
    "python argument": "An argument is a value we pass to a function or a method when calling it. In Python, "
                       "we have the following kinds of arguments:",
    "Attribute": "An attribute is a value an object holds. We can access an object’s attributes using the dot operator "
                 "(.).",
    "Duck-Typing": "If it looks like a duck, then it is a duck",
    "f-string": "An f-string is a formatted string literal. To write these, we precede a string with the letter "
                "‘f’ or ‘F’. This lets us put in values into a string.",
    "File Object": "A file object, in Python, is an object that exposes a file-oriented API to an underlying resource. "
                   "Such an API has methods such as read() and write().",
    "Finder": "The finder is an object that attempts to find the loader for a module that we are importing.",
}

for k, v in glossary.items():
    print("Word: \n" + str(k).title())
    print("Meaning: \n" + str(v))
    print("")

