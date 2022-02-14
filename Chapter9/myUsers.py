from user import User
from privileges import Privileges
from admin import Admin
print("""Exercise 9-5
=================================================================""")

user_login_test = User("John", "Doe", 18, "Male", "English", "user004", "admin")
for x in range(5):
    user_login_test.incriment_login_attempts()
    print(f"User {user_login_test.username} has attempted logging in {user_login_test.login_attempts} times.")
user_login_test.reset_login_attempts()
print("Attempt limit reached.")
print("Attempts reset to:", user_login_test.login_attempts)
print(f"Account {user_login_test.username} timed out for 30 minutes.")

print("""Exercise 9-7 and 9-8
=================================================================""")

admin1 = Admin("Sheckman", "Hyde", 35, "Male", "English", "admin", "Hg67@l9&&Bb9$", ["can add post", "can remove post", "can ban user", "can access user history"])
admin1.describe_user()
admin1.privileges.show_privileges()