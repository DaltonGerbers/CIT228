import unittest
from restaurant import Restaurant

class TestRestaurant(unittest.TestCase):
    def setUp(self):
        restaurant_name = "Generic Restaurant Name"
        cuisine_type = "Good"
        number_served = 1500
        self.restaurant = Restaurant(restaurant_name, cuisine_type, number_served)
    
    def test_set_number_served_int(self):
        sales = 1000
        self.restaurant.set_number_served(sales)
        self.assertEqual(self.restaurant.number_served, 1000)
    
    def test_set_number_served_string(self):
        sales = "1000"
        self.restaurant.set_number_served(sales)
        self.assertEqual(self.restaurant.number_served, 1000)
    
    def test_increment_number_served_served_float(self):
        sales = 1000.50
        self.restaurant.incriment_number_served(sales)
        self.assertEqual(self.restaurant.number_served, 2500.50)
    
    def test_increment_number_served_served_string(self):
        sales = "1000"
        self.restaurant.incriment_number_served(sales)
        self.assertEqual(self.restaurant.number_served, 2500)

if __name__ == '__main__':
    unittest.main()