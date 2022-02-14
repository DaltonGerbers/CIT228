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