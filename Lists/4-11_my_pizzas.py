#!/usr/bin/python3

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
pizzas = ["margherita", "Quatro stagioni", "Bolognese"]

friend_pizzas = pizzas[:]

# "Al funghi",
# "Pepperoni",
# "Salame",


# Then, do the following:
# •Add a new pizza to the original list.
pizzas.append("Al funghi")

# • Add a different pizza to the list friend_pizzas.
friend_pizzas.append("Pepperoni")

# • Prove that you have two separate lists. Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list.

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

# Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the sec-
# ond list. Make sure each new pizza is stored in the appropriate list

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
