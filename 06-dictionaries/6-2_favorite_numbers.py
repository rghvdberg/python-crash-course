# import the faker library
from faker import Faker

fake = Faker()

favorite_numbers = {}

for i in range(5):
    favorite_numbers[fake.name()] = fake.random_int(min=1, max=10)


print(favorite_numbers)
