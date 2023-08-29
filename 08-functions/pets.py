# NOTE
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ When you use default values, any parameter with a default value needs to be       ┃
# ┃ listed  after all the parameters that have default values. This allows Python to  ┃
# ┃ continue interpreting positional arguments correctly.                             ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


def describe_pet(animal_type: str = "dog", pet_name: str = "willie"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("hamster", "harry")
describe_pet("cat", "mario")
describe_pet(animal_type="dog", pet_name="spot")
describe_pet(pet_name="spot", animal_type="dog")
describe_pet("lizzard")
