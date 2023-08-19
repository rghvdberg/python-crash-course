# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the infor-
# mation you have stored about it.

cities = {
    "paris": {
        "country": "france",
        "population": 22000000,
        "fact": "Paris is the capital of France",
    },
    "london": {
        "country": "uk",
        "population": 8000000,
        "fact": "London is the capital of England",
    },
    "berlin": {
        "country": "germany",
        "population": 6000000,
        "fact": "Berlin is the capital of Germany",
    },
}

for city, info in cities.items():
    print(city.title())
    print("\tCountry: " + info["country"].title())
    print("\tPopulation: " + str(info["population"]))
    print("\tFact: " + info["fact"])
