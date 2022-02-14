class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"User's privileges are:")
        for x in self.privileges:
            print(" -",x)