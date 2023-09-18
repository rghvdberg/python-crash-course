from pathlib import Path
import json

path = Path("user.json")
if path.exists():
    contents = path.read_text()
    user = json.loads(contents)
    for key, value in user.items():
        print(f"{key}: {value}")
else:
    username = input("What is your name? ")
    email = input("What is your email address? ")
    location = input("What is your location? ")
    user = {
        "username": username,
        "email": email,
        "location": location,
    }
    contents = json.dumps(user)
    path.write_text(contents)
    print(f"We'll remember you  when you come back, {username}!")
