import unittest
from city_functions import city_combine

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        city_nation = city_combine('changde','china')
        self.assertEqual(city_nation,'Changde,China')

    def test_city_country_population(self):
        city_nation = city_combine('changde','china',80000)
        self.assertEqual(city_nation,'Changde,China - population 80000')

unittest.main()
