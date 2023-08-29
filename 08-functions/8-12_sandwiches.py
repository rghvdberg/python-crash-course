# 8-12 Sandwiches


# This functions accepts an arbitrary number of arguments and prints out a
# summary of the sandwich being ordered.
def make_sandwich(*ingredients):
    """Summarize the sandwich we are about to make."""
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient.title()}")


# call the function make_sandwich three times, each time with a different
# number of ingredients

make_sandwich("bacon")
make_sandwich("bacon", "lettuce", "cheese")
make_sandwich("bacon", "lettuce", "tomato", "cheese")
