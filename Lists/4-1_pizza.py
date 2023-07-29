#!/usr/bin/python3

# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store
# pizza names in a list, and then use a for loop to print the name of each
# pizza.

pizzas = [
    "margherita",
    "Quatro stagioni",
    "Bolognese",
    "Al funghi",
    "Pepperoni",
    "Salame",
]

for pizza in pizzas:
    print(pizza)


# * Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.

print("")

for pizza in pizzas:
    print("I like pizza " + pizza.title() + ".")

#  * Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!

print("")

print("I like Quatro stagioni pizza.")
print("Pizza Salame is one of my favorites.")
print("I should eat pizza Salame soon.")
print("I really love pizza!")
