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


class IceCreamStand(Restaurant):
    """Model an Ice Cream Stand"""

    def __init__(self, name, cuisine_type="Ice Cream"):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def add_flavor(self, *flavors):
        for flavor in flavors:
            self.flavors.append(flavor)

    def list_flavors(self):
        print(f"{self.name.title()} serves the following ice cream flavors:")
        for flavor in self.flavors:
            print(f"\t * {flavor.title()}")


my_restaurant = IceCreamStand("Olaf")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.add_flavor("vanilla", "strawberry", "chocolate", "stragiatelli")
my_restaurant.list_flavors()
