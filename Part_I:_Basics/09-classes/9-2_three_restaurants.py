# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different in


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # Make a method called describe_restaurant() that prints these two pieces of
    # information,

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name.title()}")
        print(f"Cuisine type: {self.cuisine_type.title()}")

    #            , and a method called open_restaurant() that prints a message indi-
    # cating that the restaurant is open.

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open.")


# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.


# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

restaurants = [
    Restaurant("MacDonalds", "fast food"),
    Restaurant("de kleine griek", "griek"),
    Restaurant("mama mia!", "pasta"),
]

for restaurant in restaurants:
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
