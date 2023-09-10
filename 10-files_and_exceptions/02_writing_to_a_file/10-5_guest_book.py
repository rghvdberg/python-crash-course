from pathlib import Path

guest_book = ""
prompt = "Input your name or type 'q' to quit :"
while True:
    name = input(prompt)
    if name == "q":
        break
    else:
        guest_book += f"{name}\n"


path = Path("guest_book.txt")
path.write_text(guest_book)

contents = path.read_text()
print(contents)
