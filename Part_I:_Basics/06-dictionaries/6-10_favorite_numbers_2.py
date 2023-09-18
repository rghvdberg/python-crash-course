from faker import Faker
from random import randint

fake = Faker()

favorite_numbers = {}

for i in range(5):
    numbers_list = list({randint(1, 100) for _ in range(randint(1, 5))})
    numbers_list.sort()
    favorite_numbers[fake.name()] = numbers_list

for person, numbers in favorite_numbers.items():
    print(f"{person}'s favorite numbers are: {', '.join(map(str, numbers))}")
