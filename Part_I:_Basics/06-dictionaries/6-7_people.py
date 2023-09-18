# import the faker library
from faker import Faker

fake = Faker("nl_NL")

people = []
for _ in range(2):
    person = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "age": fake.random_int(min=18, max=99),
        "city": fake.city(),
    }
    people.append(person)

for person in people:
    print(f"First Name: {person['first_name'].capitalize()}")
    print(f"Last Name: {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")
    print("\n")
