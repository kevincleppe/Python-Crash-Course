import unittest
from ch11_1 import get_city_country

class citycheck(unittest.TestCase):

    def test_name(self):
        city_country=get_city_country('redlands', 'california','123123')
        self.assertEqual(city_country, 'Redlands California 123123')

        city_country=get_city_country('yucaipa', 'california', '321')
        self.assertEqual(city_country, 'Yucaipa California 321')

        city_country=get_city_country('yucaipa', 'california', '321')
        self.assertNotEqual(city_country, 'Yucaipa California 321')

        city_country=get_city_country('tokyo','korea','3')
        self.assertNotEqual=(get_city_country,'Tokyo Korea 3')

if __name__ == '__main__':
    unittest.main()