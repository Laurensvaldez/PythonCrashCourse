# Magicians
# Make a list of magician's names. Pass the list to a function called show_magicians(), which prints the name of each
# magician in the list.

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

magicians = ['houdini', 'klok', 'edward']
show_magicians(magicians)