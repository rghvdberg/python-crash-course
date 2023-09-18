# 7-10
# Dream Vacation
dream_vacation = {}
while True:
    name = input("What is your name? ")
    location = input("Where do you want to vacation? ")
    dream_vacation[name] = location
    more = input("Do you want to add more people? ")
    if more == "no":
        break

for name, location in dream_vacation.items():
    print(f"{name} wants to go to {location}.")
