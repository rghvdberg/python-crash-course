from pathlib import Path
import json

favorite_number = input("What is your favorite number? ")
favorite_number = int(favorite_number)
path = Path("favorite_number.json")
contents = json.dumps(favorite_number)
path.write_text(contents)
