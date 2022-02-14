from restaurant import Restaurant
from icecream import IceCreamStand
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

print("""Exercise 9-6
=================================================================""")
ice_cream_stand = IceCreamStand("Joe's Stand", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry", "Mint"])
ice_cream_stand.display_flavors()