class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine_type attributes."""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f"{self.name} is now open.")


my_restaurant = Restaurant("Burger King", "Fast Food")

print(f"\n{my_restaurant.name} serves {my_restaurant.cuisine_type} cuisine.")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
