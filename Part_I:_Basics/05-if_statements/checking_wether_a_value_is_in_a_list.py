toppings = ["mushrooms", "onions", "pinaple"]

topping = "mushrooms"
if topping in toppings:
    print(f"{topping} is in toppings[]")
else:
    print(f"{topping} is not in toppings")

topping = "ansjovis"

if topping not in toppings:
    print(f"{topping} is not in toppings[]")
else:
    print(f"{topping} is in toppings")
