#!/usr/bin/python3

alien_colors = ["green", "yellow", "red"]

for alien_color in alien_colors:
    print(f"Alien Color is {alien_color}")
    if alien_color == "green":
        print("You earned 5 points!")
    elif alien_color == "yellow":
        print("You earned 10 points!")
    else:
        print("Yea earned 15 points!")
