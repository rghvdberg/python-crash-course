# Using int() to Accept Numerical Input

height = input("How tall are you, in cm? ")
height = int(height)

if height >= 100:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'l be able to ride when you're a little older.")
