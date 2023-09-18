#!/usr/bin/python3

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# TUPLES ARE IMMUTABLE
# dimensions[0] = 25
# "__setitem__" method not defined on type "tuple[Literal[200], Literal[50]]"

# Looping
print("\nLooping:")
for dimension in dimensions:
    print(dimension)

print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
