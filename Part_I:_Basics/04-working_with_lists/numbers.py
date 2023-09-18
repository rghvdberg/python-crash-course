#!/usr/bin/python3

# Making Numerical Lists
# print 1 ... 4
for value in range(1, 5):
    print(value)

# 1 ... 5
for value in range(1, 6):
    print(value)

# range() to Make a List of Numbers

numbers = list(range(1, 6))
print(numbers)

# skip numbers range(start,stop,step)
even_numbers = list(range(2, 11, 2))
print(even_numbers)
