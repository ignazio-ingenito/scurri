# -*- coding: utf-8 -*-

"""Multiple module

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

class Multiple(object):

    @classmethod
    def is_multiple_of(cls, n: int, x: int) -> bool:
        """Check if n is multiple of x."""
        return n % x == 0

    @classmethod
    def check_number(cls, n: int) -> str:
        if n in (None, 0):
            raise Exception(f'Invalid parameter value: {n}')

        result = ""
        # check if is multiple of 3
        if Multiple.is_multiple_of(n, 3):
            result += "Three"
        if Multiple.is_multiple_of(n, 5):
            result += "Five"

        return str(n) if result == "" else result

    @classmethod
    def print_numbers(cls, max: int):
        """Return numbers from 1 to n, printing:

           Multiple of 3: Print "Three"
           Multiple of 5: Print "Five"
           Multiple of 3 and 5: Print "ThreeFive"

           Keywords arguments:
           n: Integer threshold

           Return:
           an iterator which cares about the range
        """
        nums = [Multiple.check_number(n) for n in range(1, max + 1)]

        for num in nums:
            print(num)


if __name__ == "__main__":
    Multiple.print_numbers(100)


