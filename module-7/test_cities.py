# Made by: Samuel Sidzyik
# Module 7.2 Assignment.py
# Start Date February 12, 2026
# Finished 2/22/26

# Learning unit testing with simple print of country information

import unittest
'Had to rename my file from 7.2.py  to 7_2.py because it has issues reading periods....'
from Sidzyik_Module_7_2 import get_formatted_locale

class LocationTestCase(unittest.TestCase):

    def test_city_country(self):
        "Does this locale work?"
        formatted_locale = get_formatted_locale('London', 'england')
        self.assertEqual(formatted_locale, 'London, England')

    def test_city_country_pop(self):
        "Does this locale work?"
        formatted_locale = get_formatted_locale('Rome', 'Italy', '2750000')
        self.assertEqual(formatted_locale, 'Rome, Italy - population 2750000')

    def test_city_country_pop_lang(self):
        "Does this locale work?"
        formatted_locale = get_formatted_locale('santiago', 'chile','5000000','Spanish')
        self.assertEqual(formatted_locale, 'Santiago, Chile - population 5000000, Spanish')

if __name__ == "__main__":
    unittest.main()