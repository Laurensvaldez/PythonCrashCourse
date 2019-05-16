# Pets
# First we make an empty list in which we will store the pets
pets = []

pet = {
    "animal": "chiba",
    "animal-kind": "dog",
    "pet owner": "laurens",
}
pets.append(pet)

pet = {
    "animal": "zen",
    "animal-kind": "rabbit",
    "pet owner": "elba",
}
pets.append(pet)

pet = {
    "animal": "tygo",
    "animal-kind": "cat",
    "pet owner": "franchesca",
}
pets.append(pet)

for pet in pets:
    name = pet["animal"]
    kind = pet["animal-kind"]
    owner = pet["pet owner"]
    print("The animal's name is " + name.title() + " and it's a " + kind + " the owner's name is " + owner.title()
          + ".")