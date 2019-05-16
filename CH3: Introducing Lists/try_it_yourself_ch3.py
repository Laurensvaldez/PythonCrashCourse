# this is the try it yourself challenge file

print ("3-1")

namen_lijst = ['Elba', 'Laurens', 'Estefania', 'Lopez', 'Salcedo', 'Valdez']

for x in namen_lijst:
    print (x)

# for this exercise I used the for loop, something that has not been discussed yet
# the challenge was to store the names in a list and to print each one out
# with the for loop each name will be printed one by one

print ("3-2")

for x in namen_lijst:
    print ("Hello " + x + " welcome to Python!")

# for this exercise I also used the for loop
# see where the x is placed for the placement of the name of each value in the list

print ("3-3")

motorcycle_list = ["Kawasaki", "Suzuki", "Aprilia", "Harley-Davidson", "Honda"]

for motor in motorcycle_list:
    print ("I would like to own a " + motor + " motorcycle.")

print("3-4")
to_eat = ["Rosanne Kijkuit", "Liselot Zieleman", "Frank Menduapessy"]

def invitation_dinner():
    print ("I would like to have a dinner with " + to_eat[0] + ", because she was fun and I never had the opportunity to take her out for dinner.")
    print("I would like to have a dinner with " + to_eat[1] + ", because she died so suddenly and I miss her.")
    print("I would like to have a dinner with " + to_eat[2] + ", because I never had the chance to say goodbye.")
invitation_dinner()

print("3-5")

print(to_eat[1] + " won't be able to make it to the dinner.")
to_eat.pop(1)
to_eat.insert(1,"Juju Salcedo Valdez")

def invitation_dinner_2():
    print("I would like to have a dinner with " + to_eat[0] + ", because she was fun and I never had the opportunity to take her out for dinner.")
    print("I would like to have a dinner with " + to_eat[1] + ", because he died so suddenly and I never got the chance to meet him.")
    print("I would like to have a dinner with " + to_eat[2] + ", because I never had the chance to say goodbye.")

invitation_dinner_2()

print("3-6")
print("I would like to inform the invited guests, that I have found a bigger dinning table.")
to_eat.insert(0, "Elba Estefania Toranzo Lopez")
to_eat.insert(1, "Ruth Virginia Hidalgo")
to_eat.insert(-1, "Rafael Diaz Moreno")

for x in to_eat:
    print("I would like to have a dinner with " + x + ", because he or she has a special meaning in my life.")


print("3-7")

print("Unfortunaly I only have place for two guests.")

cancelled_invite= to_eat.pop()
print("I'm sorry " + cancelled_invite + " the invitation is off. ")

cancelled_invite= to_eat.pop()
print("I'm sorry " + cancelled_invite + " the invitation is off. ")

cancelled_invite= to_eat.pop()
print("I'm sorry " + cancelled_invite + " the invitation is off. ")

cancelled_invite= to_eat.pop()
print("I'm sorry " + cancelled_invite + " the invitation is off. ")
print("\n")

for x in to_eat:
    print("Dear " + x + " you are welcome to join for dinner.")

del to_eat[::]

print(to_eat)

# page 41 - 47 for information about modifying data structures
