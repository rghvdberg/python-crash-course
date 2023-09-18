from pathlib import Path

path = Path("moby_dick.txt")
contents = path.read_text()
wc = contents.lower().count("the ")

print(wc)
