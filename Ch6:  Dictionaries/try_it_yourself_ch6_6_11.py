# Cities

cities = {
    "San Francisco": {"country": "usa", "population": 884363, "fact": "whatever"},
    "Los Angeles": {"country": "usa", "population": 4000000, "fact": "whatevera"},
    "New York": {"country": "usa", "population": 8623000, "fact": "whateverb"}
}

for city, info in cities.items():
    print("The city of " + city.title() + ": ")
    for information in info:
        location = info["country"]
        people = str(info["population"])
        facts = info["fact"]
    print("Is located in: " + location.upper())
    print("Has a population of: " + people)
    print("And the fact is: " + facts.title())
    print("")