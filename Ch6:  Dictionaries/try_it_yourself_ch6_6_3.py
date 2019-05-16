# Glossary

glossary = {
    "concatenate": "When you patch strings, integers or floats together.",
    "indexing": "When you request a certain value by determining the position.",
    "dictionary": "In this case a data structure system in which keys with their values are stored.",
    "list": "As a dictionary, but without the use of keys and only objects, string, integers are stored",
    "for-loop": "The use of a function that enables the user to use loops in codes.",
}

for k, v in glossary.items():
    print("Word: \n" + str(k).title())
    print("Meaning: \n" + str(v))
    print("")
