# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# •Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# •Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

glossary = {
    "list": "a collection of objects",
    "tuple": "a collection of objects that cannot be changed",
    "dictionary": "a collection of key-value pairs",
    "if statement": "a conditional statement",
    "for loop": "a loop that repeats a block of code for a given number of times",
}


for word in glossary:
    print(f"{word}: {glossary[word]}")

for word, meaning in glossary.items():
    print(f"{word}: {meaning}")
