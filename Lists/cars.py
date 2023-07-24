#!/usr/bin/python3
# Organizing a List

# sort() Method

cars =['bmw','audi','toyota','subaru']
print("Before sort()")
print(cars)

cars.sort()
print("After sort()")
print(cars)

# reverse sort
cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function


cars = ['bmw', 'audi', 'toyota', 'subaru']

print(sorted(cars))

# Reverse Order

cars.reverse()
print(cars)

# Finding the Length of a List
print ( len(cars) )
