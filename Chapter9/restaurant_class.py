class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(self.restaurant_name + " serves " + self.cuisine_type + " cuisine.")

    def open_restaurant(self):
        print(self.restaurant_name + " is now open.")

print("""Exercise 9-1
=================================================================""")

restaurant = Restaurant("Taco Bell", "Americanized Mexican")
print("""Restaurant= Taco Bell
Cuisine= Americanized Mexican""")
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("""Exercise 9-2
=================================================================""")

restaurant1 = Restaurant("China Buffet", "Chinese")
restaurant2 = Restaurant("Cracker Barrel", "American")
restaurant3 = Restaurant("Mancino's", "Americanized Italian")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()