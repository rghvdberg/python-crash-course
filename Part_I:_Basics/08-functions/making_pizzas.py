# # NOTE:
# # Importing an Entire Module

# import pizza

# pizza.make_pizza(25, "pepperoni")
# pizza.make_pizza(35, "mushrooms", "green peppers", "extra cheese")


# # NOTE:
# # Importing Specific Functions

# from pizza import make_pizza
#
# make_pizza(25, "pepperoni")
# make_pizza(35, "mushrooms", "green peppers", "extra cheese")

# NOTE:
# # Using as to Give a Function an Alias
#
# from pizza import make_pizza as mp
#
# mp(25, "pepperoni")
# mp(35, "mushrooms", "green peppers", "extra cheese")

# NOTE:
# Using as to Give a Module an Alias

# import pizza as p
#
# p.make_pizza(25, "pepperoni")
# p.make_pizza(35, "mushrooms", "green peppers", "extra cheese")

# NOTE:
# Importing All Functions from a Module

from pizza import *

make_pizza(25, "pepperoni")
make_pizza(35, "mushrooms", "green peppers", "extra cheese")
