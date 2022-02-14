class Resteraunt:
    def __init__(self, resteraunt_name, cuisine_type, number_served = 0):
        self.resteraunt_name = resteraunt_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_resteraunt(self):
        print(self.resteraunt_name + " serves " + self.cuisine_type + " cuisine.")

    def open_resteraunt(self):
        print(self.resteraunt_name + " is now open.")

    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def incriment_number_served(self, number_served_today):
        self.number_served = self.number_served + number_served_today

print("""Exercise 9-4
=================================================================""")
resteraunt = Resteraunt("Mancino's", "Americanized Italian")
resteraunt.describe_resteraunt()
resteraunt.open_resteraunt()
print("Customers served without changes =",resteraunt.number_served)
resteraunt.number_served = 5
print("Customers served after set to 5 =",resteraunt.number_served)
resteraunt.set_number_served(int(input("How many were served: ")))
print("Customers served after set =",resteraunt.number_served)
resteraunt.incriment_number_served(int(input("How many additionally were served today: ")))
print("Customers served after incrimented =",resteraunt.number_served)