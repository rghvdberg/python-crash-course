# 8-14. Cars: Write a function that stores information about a car in a diction-
# ary. The function should always receive a manufacturer and a model name. It


def car(manufacturer, model, **car):
    car["manufacturer"] = manufacturer
    car["model"] = model
    return car


my_car = car("Renault", "Zoe", color="Champagne", engine="Electric")

for key, value in my_car.items():
    print(f"{key} : {value}")
