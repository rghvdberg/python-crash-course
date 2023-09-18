from pathlib import Path


def read_file(filename):
    path = Path(filename)
    try:
        contents = path.read_text().rstrip()
    except FileNotFoundError:
        print(f"Sorry, I can't find {filename}! 😱")
    else:
        print(contents)


filenames = ["cats.txt", "dogs.txt", "birds.txt"]

for filename in filenames:
    read_file(filename)
