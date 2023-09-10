# 10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a ValueError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the ValueError if
# either input value is not a number, and print a friendly error message. Test your
# program by entering two numbers and then by entering some text instead of a
# number.


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


while first_number == "ValueError":
    first_number = input("Enter 1st number: ")
    first_number = isInteger(first_number)

while second_number == "ValueError":
    second_number = input("Enter 2nd number: ")
    second_number = isInteger(second_number)

answer = first_number + second_number
print(f"{first_number} + {second_number} = {answer}")
