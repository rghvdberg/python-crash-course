#!/bin/python3

from random import randint

for _ in range(0, 10):
    age = randint(0, 100)
    print(f"The persons age is {age}.")
    stage = ""
    if age < 2:
        stage = "baby"
    elif age >= 2 and age < 4:
        stage = "toddler"
    elif age >= 4 and age < 13:
        stage = "kid"
    elif age >= 13 and age < 20:
        stage = "teenager"
    elif age >= 20 and age < 65:
        stage = "adult"
    else:
        stage = "elder"

    print(f"The persons stage of life is called: {stage}.\n")
