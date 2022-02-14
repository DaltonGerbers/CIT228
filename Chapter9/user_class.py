class User:
    def __init__(self, first_name, last_name, age, gender, language_spoken, username, password, login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.language_spoken = language_spoken
        self.username = username
        self.password = password
        self.login_attempts = login_attempts
        if (gender == "Male"):
            self.pronoun = "His"
        elif (gender == "Female"):
            self.pronoun = "Her"
        else:
            self.pronoun = "Their"

    def describe_user(self):
        print(f"User {self.last_name}, {self.first_name} is a {self.age} year old {self.gender} who speaks {self.language_spoken}: {self.pronoun} username is \"{self.username}\" and password is \"{self.password}\"")
    
    def greet_user(self):
        if(self.language_spoken == "Spanish"):
            print(f"Hola, {self.first_name} {self.last_name}, disfruta de la aplicación.")
        elif(self.language_spoken == "German"):
            print(f"Hallo, {self.first_name} {self.last_name}, viel Spaß mit der Anwendung.")
        else:
            print(f"Hello, {self.first_name} {self.last_name}, enjoy the application.")
    
    def incriment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Dan", "Tyler", 23, "Male", "English", "Danimals", "Zak+Cody")
user2 = User("Hue", "Rodriguez", 60, "Male", "Spanish", "Hue", "Password")
user3 = User("Lacey", "Schmidt", 27, "Female", "German", "PanzerMensch", "Qb7&@1mmnIL89*&")
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()

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