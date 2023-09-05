# 10-1 Learning Python

from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()

for line in contents.splitlines():
    print(line)

# 10-2 Learning C

for line in contents.splitlines():
    print(line.replace("Python", "C"))


# pi_string

path = Path("pi_million_digits.txt")
contents = path.read_text()
pi_string = ""
for line in contents.splitlines():
    pi_string += line.lstrip()

print(f"{pi_string[:52]}")

print(len(pi_string))
