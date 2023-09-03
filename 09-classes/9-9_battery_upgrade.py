class Car:
    """A simple attempt at modeling a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describa a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's milage"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """
        Set the odometer reading tot the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount tot the odometer reading."""
        self.odometer_reading += miles


# NOTE: class Car as argument in class declartion
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        # NOTE: self.battery is an instance of class Battery()
        self.battery = Battery()


class Battery:
    """
    A simple attempt to model a battery for an electric car
    """

    def __init__(self, battery_size=40) -> None:
        """
        Initialize the battery's attributes
        """
        self.battery_size = battery_size

    def describe_battery(self):
        """
        Print a a statement describing the battery size.
        """
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """
        Print a statement about the range this battery provides.
        """
        range = 0
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65


my_car = ElectricCar("renault", "zoe", 2013)
print(my_car.get_descriptive_name())

# NOTE: syntax here <instance of ElectricCar>.<instance of <Battery>.method of Battery
my_car.battery.describe_battery()

my_car.battery.upgrade_battery()

my_car.battery.describe_battery()
