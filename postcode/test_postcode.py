# -*- coding: utf-8 -*-

"""Postcode unittest module

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

from webapp import Postcode

VALID_POSTCODES = [
    'KT10 8BD', # already formatted - my home postcode :D
    'kt10 8bd', # lowercase no space
    'KT108BD', # uppercase no space
    'kt108bd', # lowercase no space
    "w1a0ax",  # --> Other combinations with different length from wikipedia
    "m11ae",
    "b338th",
    "cr26xh",
    "dn551pt",
]

INVALID_POSTCODES = [
    'QT10 8BD',  # Invalid: The letters QVX are not used in the first position
    'VT10 8BD',  # Invalid: The letters QVX are not used in the first position
    'XT10 8BD',  # Invalid: The letters QVX are not used in the first position
    'KI10 8BD',  # Invalid: The letters IJZ are not used in the second position
    'KJ10 8BD',  # Invalid: The letters IJZ are not used in the second position
    'KTX0 8BD',  # Invalid: only letters to appear in the third position are ABCDEFGHJKPSTUW
    'KT1C 8BD',  # Invalid: only letters to appear in the fourth position are ABEHMNPRVWXY
    'KT10 9CZ',  # Invalid: inward code do not use CIKMOV
    'BBB 9CZ',  # Invalid: all letters in outward code
    '1111 9CZ',  # Invalid: all digits in Outward code
    '99AA 1AA',  # Invalid: all Digits post code area
    'AA1 AA',  # Invalid: all letters in inward code,
]

class TestPostCode(unittest.TestCase):

    def setUp(self) -> None:
        """Setup the unit test module

           to test more then the first 100 values increase the self.max attribute
        """
        self.postcode = Postcode()

    def test_validate_with_valid_postcodes(self):
        for code in  VALID_POSTCODES:
            self.postcode.validate(code)
            self.assertTrue(self.postcode.is_valid)
            self.assertTrue(self.postcode.message.startswith('VALID'))

    def test_format_with_valid_postcodes(self):
        for code in  VALID_POSTCODES:
            self.postcode.format(code)
            self.assertTrue(self.postcode.message == 'Formatted')

    def test_split_validate_with_valid_postcodes(self):
        for code in  VALID_POSTCODES:
            self.postcode.split_validate(code)
            self.assertTrue(self.postcode.message.startswith('VALID'))
            self.assertTrue(self.postcode.postcode_area != '')
            self.assertTrue(self.postcode.postcode_district != '')
            self.assertTrue(self.postcode.postcode_sector != '')
            self.assertTrue(self.postcode.postcode_unit != '')

    def test_validate_with_empty_string(self):
        self.postcode.validate('')
        self.assertTrue(self.postcode.message == 'ERROR: length must be minimum 5 and maximum 8')

    def test_validate_with_none(self):
        self.postcode.validate(None)
        self.assertTrue(self.postcode.message == 'ERROR: length must be minimum 5 and maximum 8')

    def test_format_with_W1A0AX(self):
        self.postcode.format('w1a0ax')
        self.assertTrue(self.postcode.fmt_postcode == "W1A 0AX")

    def test_validate_with_W1A0AX(self):
        self.postcode.validate('w1a0ax')
        self.assertTrue(self.postcode.is_valid)
        self.assertTrue(self.postcode.fmt_postcode == "W1A 0AX")

    def test_validate_with_W1A0AX(self):
        self.postcode.split_validate('w1a0ax')
        self.assertTrue(self.postcode.is_valid)
        self.assertTrue(self.postcode.message.startswith('VALID'))
        self.assertTrue(self.postcode.fmt_postcode == "W1A 0AX")
        self.assertTrue(self.postcode.outward_code == "W1A")
        self.assertTrue(self.postcode.inward_code == "0AX")
        self.assertTrue(self.postcode.postcode_area == "W")
        self.assertTrue(self.postcode.postcode_district == "1A")
        self.assertTrue(self.postcode.postcode_sector == "0")
        self.assertTrue(self.postcode.postcode_unit == "AX")

    def test_validate_with_invailid_length_code(self):
        self.postcode.split_validate('EC1A 1BB999')
        self.assertFalse(self.postcode.is_valid)
        self.assertFalse(self.postcode.message.startswith('VALID'))

        self.postcode.split_validate('EC1A1BB999')
        self.assertFalse(self.postcode.is_valid)
        self.assertFalse(self.postcode.message.startswith('VALID'))

    def test_validate_with_invalid_character(self):
        self.postcode.split_validate('$C1A 1BB')
        self.assertFalse(self.postcode.is_valid)
        self.assertFalse(self.postcode.message.startswith('VALID'))

        self.postcode.split_validate('E?1A1BB')
        self.assertFalse(self.postcode.is_valid)
        self.assertFalse(self.postcode.message.startswith('VALID'))

        self.postcode.split_validate('EC!A1BB')
        self.assertFalse(self.postcode.is_valid)
        self.assertFalse(self.postcode.message.startswith('VALID'))

        self.postcode.split_validate('EC1# 1BB')
        self.assertFalse(self.postcode.is_valid)
        self.assertFalse(self.postcode.message.startswith('VALID'))

        self.postcode.split_validate('EC1A @BB')
        self.assertFalse(self.postcode.is_valid)
        self.assertFalse(self.postcode.message.startswith('VALID'))

        self.postcode.split_validate('EC1A1*B')
        self.assertFalse(self.postcode.is_valid)
        self.assertFalse(self.postcode.message.startswith('VALID'))

        self.postcode.split_validate('EC1A1B+')
        self.assertFalse(self.postcode.is_valid)
        self.assertFalse(self.postcode.message.startswith('VALID'))

    def test_validate_with_invalid_postcodes(self):
        for code in INVALID_POSTCODES:
            self.postcode.validate(code)
            if self.postcode.is_valid:
                print(code)
            self.assertFalse(self.postcode.is_valid)
            self.assertFalse(self.postcode.message.startswith('VALID'))



if __name__ == "__main__":
     unittest.main()