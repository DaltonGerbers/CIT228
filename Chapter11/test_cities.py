import unittest
from city_functions import get_formatted_city

class CityTestCase(unittest.TestCase):
    def test_country_city(self):
        formatted_city = get_formatted_city('berlin', 'germany')
        self.assertEqual(formatted_city, 'Berlin, Germany')

    def test_country_city_population(self):
        formatted_city = get_formatted_city('berlin', 'germany', '3,645,000')
        self.assertEqual(formatted_city, 'Berlin, Germany - population 3,645,000')

if __name__ == '__main__':
    unittest.main()