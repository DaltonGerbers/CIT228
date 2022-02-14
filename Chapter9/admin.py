from user import User
from privileges import Privileges
class Admin(User):
    def __init__(self, first_name, last_name, age, gender, language_spoken, username, password, privileges, login_attempts = 0):
        super().__init__(first_name, last_name, age, gender, language_spoken, username, password, login_attempts)
        self.privileges = Privileges(privileges)