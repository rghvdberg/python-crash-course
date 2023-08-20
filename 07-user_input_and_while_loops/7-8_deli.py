# list of various sandwiches

sandwich_orders = ["chicken", "veggie", "turkey", "pork"]
finished_sandwich = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich}")
    finished_sandwich.append(current_sandwich)

for sandwich in finished_sandwich:
    print(f"I made a {sandwich} sandwich.")
