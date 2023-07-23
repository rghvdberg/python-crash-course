#!/usr/bin/python3

# Modifying Elements in a List

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)


motorcycles[0] = 'ducati'
print(motorcycles)

# Adding Elements to a List

# add to the end
motorcycles.append('ducati')
print(motorcycles)

# Inserting Elements into a List
motorcycles.insert(1,'bmw')
print(motorcycles)

# Removing Elements from a List

# Using del
del motorcycles[0]
print(motorcycles)

# Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle  = motorcycles.pop()
print(motorcycles,popped_motorcycle)

# Pop by Index
popped_motorcycle = motorcycles.pop(0)
print(motorcycles,popped_motorcycle)

# Removing an Item by Value

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)


