#!/bin/python3

# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write
# a series of independent if statements that check for certain fruits in your
# list.

from random import randint

fav_fruits = ["apple", "banana", "orange"]

list_of_fruits = [
    "apple",
    "banana",
    "orange",
    "grape",
    "strawberry",
    "blueberry",
    "raspberry",
    "mango",
    "pineapple",
    "lemon",
]

for _ in range(0, 20):
    random_fruit = list_of_fruits[randint(0, len(list_of_fruits) - 1)]
    print(f"This is a random fruit: {random_fruit}")
    if random_fruit in fav_fruits:
        print(f"You really like {random_fruit}!")
    else:
        print(f"You don't care too much about {random_fruit}\n")
