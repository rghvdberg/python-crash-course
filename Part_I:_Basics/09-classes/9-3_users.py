# 9-3. Users: Make a class called User. Create two attributes called
# first_name # and last_name, and then create several other attributes
# that are typically stored in a user profile. Make a method called
# describe_user() that prints a summary of the user’s information. Make
# another method called greet_user() that prints a personalized
# greeting to the user.
#
# Create several instances representing different users, and call both
# methods for each user.

from faker import Faker

fake = Faker()


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.favorite_color = ""

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Favorite coler: {self.favorite_color}")

    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello, {full_name}")


users = []
for _ in range(0, 3):
    users.append(User(fake.first_name(), fake.last_name()))

for u in users:
    u.favorite_color = fake.color_name()
    u.describe_user()
    u.greet_user()
    print("---")
