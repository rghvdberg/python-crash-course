# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers, even if they make a mistake and
# enter text instead of a numberV


def isInteger(value):
    try:
        number = int(value)
    except ValueError:
        print(f'"{value}" is not an integer')
        return "ValueError"
    else:
        return number


first_number = "ValueError"
second_number = "ValueError"

print(
    """
    Enter two integers to add together.
    Type 'quit' to exit.
    """
)

quit = False

while not quit:
    while first_number == "ValueError":
        first_number = input("Enter 1st number: ")
        if first_number == "quit":
            quit = True
            break
        first_number = isInteger(first_number)

    while second_number == "ValueError" and quit is not True:
        second_number = input("Enter 2nd number: ")
        if second_number == "quit":
            quit = True
            break
        second_number = isInteger(second_number)
    if not quit:
        answer = first_number + second_number
        print(f"{first_number} + {second_number} = {answer}")
        # reset numbers
        first_number = "ValueError"
        second_number = "ValueError"
