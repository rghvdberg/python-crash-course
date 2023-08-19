# use the faker library

from faker import Faker

# import the libary for randint
from random import randint

fake = Faker()

# empty username dictionary
usernames = {}

# create list of 10 people
# loop over username dictionary
# add key "username" to dictionary
# use the faker library to generate a username
# add a empty value for each key

for _ in range(10):
    usernames[fake.user_name()] = ""

# a list of the 5 most popular programming languages
languages = [
    "JavaScript",
    "Python",
    "Java",
    "C#",
    "TypeScript",
]

# sort the usernames dictionary
# add a programming language value to the first 5 keys
tmp_usernames = []
for username in sorted(usernames):
    tmp_usernames.append(username)

# loop over first 5 usernames
# pick a random programming language from the languages list
for i in range(5):
    usernames[tmp_usernames[i]] = languages[randint(0, 4)]

# for username, language in usernames:
# print(f"{username} - {language}")
for username, language in usernames.items():
    print(f"{username} - {language}")
    if language:
        print(f"Thanks {username} for taking the poll.\n")
    else:
        print(f"Dear {username}, please consider taking the poll.\n")
