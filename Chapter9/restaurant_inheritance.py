class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        print(self.restaurant_name + " serves " + self.cuisine_type + " cuisine.")

    def open_restaurant(self):
        print(self.restaurant_name + " is now open.")

    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def incriment_number_served(self, number_served_today):
        self.number_served = self.number_served + number_served_today

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, number_served = 0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors

    def display_flavors(self):
        print("The flavors are:")
        for x in self.flavors:
            print(" -",x)

print("""Exercise 9-6
=================================================================""")
ice_cream_stand = IceCreamStand("Joe's Stand", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry", "Mint"])
ice_cream_stand.display_flavors()