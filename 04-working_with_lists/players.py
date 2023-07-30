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
