# exit with qctive
print("\nExit with active")
active = True
price = 0
prompt = "Please enter your age or leave empty to exit: "
while active:
    age = input(prompt)
    if age:
        age = int(age)
        if age < 3:
            price = 0
        elif age < 12:
            price = 10
        else:
            price = 15
        print(f"Your ticket price is ${price}")
    else:
        active = False
        print("Exit")


# exit with quit
print("\nExit with quit")

price = 0
age = ""
prompt = "Please enter your age or type 'quit' to exit: "
while age != "quit":
    age = input(prompt)
    if age != "quit":
        age = int(age)
        if age < 3:
            price = 0
        elif age < 12:
            price = 10
        else:
            price = 15
        print(f"Your ticket price is ${price}")

# exit with break

print("\nExit with break")

price = 0
age = ""
prompt = "Please enter your age or type 'quit' to exit: "
while True:
    age = input(prompt)
    if age == "quit":
        break
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age < 12:
            price = 10
        else:
            price = 15
        print(f"Your ticket price is ${price}")
