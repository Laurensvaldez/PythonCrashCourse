# Rivers: Make a dictionary containing three major rivers and the country each river runs through.
# One key-value pair might be: "nile": "egypt".

rivers = {"nile": "egypt", "maas": "Netherlands", "missippi river": "united states"}

for river, country in rivers.items():
    print("Sentence:")
    print("The " + river.title() + " runs through " + country.title() + ".")
    print("")
    print("River name:")
    print(river.title())
    print("")
    print("Country name:")
    print(country.title())