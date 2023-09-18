# fake data via https://www.mockaroo.com/

# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# •Make a list of five or more usernames called current_users.
current_users = [
    "nberk0",
    "meglington1",
    "afarndon2",
    "cbreissan3",
    "jcull4",
    "mstitwell5",
    "eeskriet6",
    "canthes7",
    "swhitlam8",
    "trignAll9",
]
# •Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.

# randomize sort :!sort -R

new_users = [
    "cmueller5",
    "dbrelsford9",
    "ahan8",
    "pgarvan6",
    "hbuxsey0",
    "Trignall9",
    "jphilippson2",
    "canthes7",
    "eeskriet6",
    "soneile1",
    "swhitlam8",
    "gwhitwell7",
    "kacott3",
    "vedinburgh4",
]

# •Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.

lower_case_current_users = [un.lower() for un in current_users]
print(lower_case_current_users)
for new_user in new_users:
    if new_user.lower() in lower_case_current_users:
        print(f"Username {new_user} is not available")

# • Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted.
