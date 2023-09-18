# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your list
# and as you do print everything you know about each pet.

from faker import Faker

fake = Faker("nl_NL")

# list of 5 pet animals
animals = [
    "dog",
    "cat",
    "bird",
    "fish",
    "turtle",
]

pets = []

for i in range(5):
    pet = {"name": fake.first_name(), "kind": animals[i], "owner": fake.name()}
    pets.append(pet)

print(pets)

for pet in pets:
    print(f"Name: {pet['name']}")
    print(f"Kind: {pet['kind']}")
    print(f"Owner: {pet['owner']}")
