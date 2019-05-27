# -*- coding: utf-8 -*-

"""Multiple unittest module

   __author__ = "Ignazio Ingenito"
   __date__ = "2019-05-27"
   __version__ = "1.0.0"
   __maintainer__ = "Ignazio Ingenito"
   __email__ = "ignazio.ingenito@gmail.com"

   Requirements: No dependencies needed.
   Compatibility = python3

   Scurry requirements: Write a program that prints the numbers from 1 to 100. But for multiples of three print “Three”
                        instead of the number and for the multiples of five print “Five”.
                        For numbers which are multiples of both three and five print “ThreeFive”.
"""

import unittest

from run_multiple import Multiple


class TestMultiple(unittest.TestCase):

    def setUp(self) -> None:
        """Setup the unit test module

           to test more then the first 100 values increase the self.max attribute
        """
        self.max = 100
        self.multiples_of_3_and_5 = [n for n in range(1, self.max + 1) if n % 3 == 0 and n % 5 == 0]
        self.multiples_of_3 = [n for n in range(1, self.max + 1) if n % 3 == 0 and n not in self.multiples_of_3_and_5]
        self.multiples_of_5 = [n for n in range(1, self.max + 1) if n % 5 == 0 and n not in self.multiples_of_3_and_5]

    def test_multiple_with_none(self):
        """Test the check_number function with None as parameter"""
        with self.assertRaises(Exception) as context:
            Multiple.check_number(None)

        self.assertTrue('Invalid parameter value: ' in str(context.exception))

    def test_multiple_with_zero(self):
        """Test the check_number function with zero as parameter"""
        with self.assertRaises(Exception) as context:
            Multiple.check_number(0)

        self.assertTrue('Invalid parameter value: ' in str(context.exception))

    def test_multiple_of_3(self):
        """Test the check_number function with all multiples of 3"""
        for n in self.multiples_of_3:
            x = Multiple.check_number(n)
            self.assertEqual(x, "Three")

    def test_multiple_of_5(self):
        """Test the check_number function with all multiples of 5"""
        for n in self.multiples_of_5:
            x = Multiple.check_number(n)
            self.assertEqual(x, "Five")

    def test_multiple_of_3_and_5(self):
        """Test the check_number function with all multiples of 3 and 5"""
        for n in self.multiples_of_3_and_5:
            x = Multiple.check_number(n)
            self.assertEqual(x, "ThreeFive")

if __name__ == "__main__":
     unittest.main()