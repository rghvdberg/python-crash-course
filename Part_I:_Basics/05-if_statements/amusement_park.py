price = 10
age = 73
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
# else:
#     price = 5
elif age >= 65:
    price = 5

print(f"Your admission cost is ${price}.")
