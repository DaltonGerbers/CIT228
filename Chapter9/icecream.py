from restaurant import Restaurant
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, number_served = 0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors

    def display_flavors(self):
        print("The flavors are:")
        for x in self.flavors:
            print(" -",x)