from faker import Faker

faker = Faker(locale="en_US")
# make a list of five or more usernames. Use the faker package.

usernames = [faker.user_name() for _ in range(5)]
usernames.append("admin")

# usernames.clear()
print(usernames)

if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")
