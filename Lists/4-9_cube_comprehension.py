#!/usr/bin/python3

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# # first 10 cubes.

cubes = [val**3 for val in range(1, 11)]
for value in cubes:
    print(value)
