#!/usr/bin/python3

squares = []
for value in range(1, 11):
    # square = value**2
    # squares.append(square)
    squares.append(value**2)

print(squares)

# Simple Statistics with a List of Numbers
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehensions

# name = [ 'expression for value' 'for loop' ]

squares = [value**2 for value in range(1, 11)]

print(squares)
