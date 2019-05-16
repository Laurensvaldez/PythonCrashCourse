# a list is made with square brackets -> []
# for example:

names = ['Laurens', 'Elba', 'Jonathan', 'Vanessa', 'Domingo']

# if you want to access an item from the list you can use the index number

print (names[:2]        )

# in this case you print the first two items given
# because in Python the first item in a data structure begins with the 0
# with thd : in front of the 2, you indicate you want every item to be print that comes before the index 2
# 'Jonathan' is index number 2 but in Python the given index will not be printed, its used as "until index number"
# with the second part of the code .title() you can use the title function to give the value a title output
# remember the stored value will not be changed, it will only be shown that way

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."

print (message)

bicycles.append("mountainbike")
bicycles.insert(0,"gazelle")

# with the insert(0, "gazelle") you place the bicycle "gazelle" at the index number 0

print (bicycles)

bicycles.pop()

print (bicycles)

# with the del statement you can use the index number to delete a certain value

del bicycles[0]

print(bicycles)

# if we want to save the popped object you can use the next code

popped_bicycle = bicycles.pop()
print(bicycles)
print(popped_bicycle)

# you can also use the indexing method to pop a certain object from the list

first_owned = bicycles.pop(0)
print("The first bicycle I owned was a " + first_owned.title() + ".")

# you can use the "remove" method to remove an item by name, for example

bicycles.remove("cannondale")

print(bicycles)

# with the bicycles.sort() you can sort the permanently sort the order of a list
# with sorted(bicycles) you can temporarily sort the order of a list
# with the following statement you can reverse the order: bicycles.sort(reverse=True)
# for the temp solution you can you use

namen_lijst = ['Elba', 'Laurens', 'Estefania', 'Lopez', 'Salcedo', 'Valdez']

print(sorted(namen_lijst))

namen_lijst.reverse()

print(namen_lijst.sort())

print(len(namen_lijst))