import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):

    def test_city_country(self):
        result = city_country('New York', 'United States')
        self.assertEqual(result, 'New York, United States')

        result = city_country('Cancun', 'Mexico')
        self.assertEqual(result, 'Cancun, Mexico')

        result = city_country('Berlin', 'Germany')
        self.assertEqual(result, 'Berlin, Germany')

if __name__ == '__main__':
    unittest.main()
