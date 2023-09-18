# a dictionary with python keywords and their meaning
glossary = {
    "list": "a collection of objects",
    "tuple": "a collection of objects that cannot be changed",
    "dictionary": "a collection of key-value pairs",
    "if statement": "a conditional statement",
    "for loop": "a loop that repeats a block of code for a given number of times",
    "while loop": "a loop that repeats a block of code while a condition is true",
    "break statement": "used to exit a loop early",
    "continue statement": "used to continue with the next iteration of a loop",
    "pass statement": "used to do nothing at all",
    "return statement": "used to exit a function early and return a value",
    "import statement": "used to import a module",
}

for word, meaning in glossary.items():
    print(f"{word}: {meaning}")
