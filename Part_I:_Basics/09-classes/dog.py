class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog("Willie", 6)

print(f"My dog's name is  {my_dog.name.title()}.")
print(f"{my_dog.name.title()} is {my_dog.age} years old.")
my_dog.sit()

your_dog = Dog("lucy", 3)

print(f"\nYour dog's name is {your_dog.name.title()}.")
print(f"{your_dog.name.title()} is {your_dog.age} years old.")
your_dog.sit()
