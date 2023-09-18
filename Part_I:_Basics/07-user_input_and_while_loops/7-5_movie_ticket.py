# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.


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
