# Cities

def describe_city(name_city, name_country= "The Netherlands"):
    print(name_city.title() + " is in " + name_country.title() + ".")

print("City 1:")
describe_city("Amsterdam")

print("City 2:")
describe_city("Rotterdam")

print("City 3:")
describe_city("Los Angeles", name_country= "United States")
