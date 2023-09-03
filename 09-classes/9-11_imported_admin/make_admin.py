from user import Admin
from faker import Faker

fake = Faker("nl_NL")

admin_user = Admin(
    fake.first_name(), fake.last_name(), fake.user_name(), fake.email(), fake.city()
)

admin_user.describe_user()
admin_user.show_privileges()
