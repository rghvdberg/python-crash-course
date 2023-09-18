from pathlib import Path
import json


def get_stored_favorite_number(path):
    """Get stored favorite number if available"""
    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        return favorite_number
    else:
        return None


def get_new_favorite_number(path):
    """Prompt for a new favorite number."""
    favorite_number = input("What is your favorite number? ")
    favorite_number = int(favorite_number)
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    return favorite_number


def message_favorite_number():
    """Print a message with a persons favorite number"""
    path = Path("favorite_number.json")
    favorite_number = get_stored_favorite_number(path)
    if favorite_number:
        print(f"Youre favorite number is {favorite_number}!")
    else:
        favorite_number = get_new_favorite_number(path)
        print("We'll remember your favorite number.")


message_favorite_number()
