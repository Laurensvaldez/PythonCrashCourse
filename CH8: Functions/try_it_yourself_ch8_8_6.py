# City names
# Write a function called city_countr() that takes in the name of a city and its country. The function should return a
# string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value that's returned.

def city_country(city, country):
    """Return city-country pairs."""
    return (city.title() + ', ' + country.title())

city = city_country('amsterdam', 'The Netherlands')
print(city)

city = city_country('santo domingo', 'Republica Dominicana')
print(city)

city = city_country('madrid', 'Spain')
print(city)