# Made by: Samuel Sidzyik
# Module 7.2 Assignment.py
# Start Date February 12, 2026
# 
# Learning unit testing with simple print of country information

import unittest

class LocationTestCase(unittest.TestCase):

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_asdffirst_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
 

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()

if __name__ == "__main__":
    unittest.main()