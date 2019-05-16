# Favorite Places

favorite_places = {
    "elba": ["fillipijnen", "hong kong", "thailand"],
    "laurens": ["alaska", "fillipijnen", "dominicaanse republiek"],
    "jonathan": ["costa rica", "nederland", "belgië"],
}

for name, places in favorite_places.items():
    print(name.title() + "'s favorite places are: ")
    for place in places:
        print("\t" + place.title())
