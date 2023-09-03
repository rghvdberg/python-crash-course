"""A class to model admins"""

from user import User


class Priveleges:
    def __init__(self) -> None:
        self.privileges = ["can add post", "can delete post", "can ban user"]


class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Priveleges()

    def show_privileges(self):
        print(f"user {self.username} has the following privileges:")
        for privilege in self.privileges.privileges:
            print(f"\t- {privilege}")
