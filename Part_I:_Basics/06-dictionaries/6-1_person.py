# import the faker library
from faker import Faker

fake = Faker()

person = {
    "first_name": fake.first_name(),
    "last_name": fake.last_name(),
    "age": fake.random_int(min=18, max=99),
    "city": fake.city(),
}

print(person)
