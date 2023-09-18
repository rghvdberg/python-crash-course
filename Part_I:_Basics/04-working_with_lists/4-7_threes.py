#!/usr/bin/python3

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop
# to print the numbers in your list.

threes = [val * 3 for val in range(1, 11)]
for value in threes:
    print(value)
