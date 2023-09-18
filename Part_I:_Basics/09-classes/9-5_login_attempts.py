# 9-5. Login Attempts: Add an attribute called login_attempts to
# your User class from Exercise 9-3 (page 162). Write a method called
# increment_login_attempts() that increments the value of login_attempts
# by 1. Write another method called reset_login_attempts() that resets
# the value of login_attempts to 0.

# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was
# incremented properly, and then call reset_login_attempts(). Print
# login_attempts again to make sure it was reset to 0.

from faker import Faker

fake = Faker()


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.favorite_color = ""
        self.login_attempts = 0

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Favorite coler: {self.favorite_color}")
        print(f"Login Attempts: {self.login_attempts}")

    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello, {full_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User(fake.first_name(), fake.last_name())

user.favorite_color = fake.color_name()
user.describe_user()
user.greet_user()
print("---")
for _ in range(5):
    user.increment_login_attempts()
    print(f"Login Attempts: {user.login_attempts}")

user.reset_login_attempts()

print("---")
user.describe_user()
