#!/usr/bin/python3

# Slicing a list

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
# ['charles', 'martina', 'michael']

print(players[1:4])
# ['martina', 'michael', 'florence']

print(players[:4])
# ['charles', 'martina', 'michael', 'florence']

print(players[2:])
# ['michael', 'florence', 'eli']

# Looping throuhg a slice

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a list

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite")
print(friend_foods)

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite")
print(friend_foods)
