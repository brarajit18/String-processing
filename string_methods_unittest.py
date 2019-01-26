# -*- coding: utf-8 -*-
import unittest
import string_methods

class StringMethods(unittest.TestCase):
    """This class used to unit test string_methods.py
    """    
    def test_processStrings(self):
        self.assertEqual(string_methods.processStrings('EEaaLbbccddXXL'), 'E2a2L2b2c2d2X2')

if __name__ == '__main__':
    unittest.main()
