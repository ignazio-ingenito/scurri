# -*- coding: utf-8 -*-

"""Postcode module

   __author__ = "Ignazio Ingenito"
   __date__ = "2019-05-27"
   __version__ = "1.0.0"
   __maintainer__ = "Ignazio Ingenito"
   __email__ = "ignazio.ingenito@gmail.com"

   Requirements: No dependencies needed.
   Compatibility = python3

   Scurry requirements: Write a library that supports validating and formatting post codes for UK.
                        The details of which post codes are is_valid and which are the parts they consist of can be found
                        at https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting.
                        The API that this library provides is your choice.
"""
import re


class Postcode(object):
    """ Class PostCode manage validation and formatting for UK post codes
        Attributes:
            in_postcode: postcode to be checked and validated
            fmt_postcode: A string to contain the proper formatted version of the post code
            outward_code: The outward code is the part of the postcode before the single space in the middle.
                          It is between two and four characters long. Examples of outward codes include
                          "L1", "W1A", "RH1", "RH10" or "SE1P". A few outward codes are non-geographic,
                          not divulging where mail is to be sent.
            inward_code: The inward code is the part of the postcode after the single space in the middle. It is three
                         characters long.
                         The inward code assists in the delivery of post within a postal district.
                         Examples of inward codes include "0NY", "7GZ", "7HF", or "8JQ".
            postcode_area: The postcode area is part of the outward code. The postcode area is either one or two
                           characters long and is all letters.
                           Examples of postcode areas include L for Liverpool, RH for Redhill and EH for Edinburgh.
                           A postal area may cover a wide area, for example "RH" covers north Sussex, and "BT" (Belfast)
                           covers the whole of Northern Ireland.
            postcode_district: The postcode district is made of one or two digits or a digit followed by a letter.
                               The outward code is between two and four characters long.
                               Examples include "W1A", "RH1", "RH10" or "SE1P".
            postcode_sector: The postcode sector is made up of single digit.
            postcode_unit: The postcode unit is two characters added to the end of the postcode sector.
                           Postcode unit generally represents a street, part of a street, a single address, a
                           group of properties, a single property, a sub-section of the property, an individual
                           organisation or (for instance Driver and Vehicle Licensing Agency) a subsection of the
                           organisation.
                           The level of discrimination is often based on the amount of mail received by the premises or
                           business.
                           Examples of postcode units include "SW1W 0NY", "PO16 7GZ", "GU16 7HF", or "L1 8JQ"
            is_valid: A boolean flag to state if the postcode is valid or not
            message: A string that contains the status of the postcode
        """

    # Format Acceptable : AA9A 9AA | A9A 9AA | A9 9AA | A99 9AA | AA9 9AA | AA99 9AA
    # from -> https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Validation

    # Postcode validation rules:
    # 1. 1st position -> letters QVX are not used
    # 2. 2nd position -> letters IJZ are not used
    # 3. 3rd position -> only ABCDEFGHJKPSTUW are used when the structure starts with A9A
    # 4. 4th position -> only ABEHMNPRVWXY are used when the structure starts with AA9A
    # 5. Last two letters in inward code never use CIKMOV

    POSTCODE_REGEX = r"^(GIR ?0AA|[A-PR-UWYZ]([0-9]{1,2}|([A-HK-Y][0-9]([0-9ABEHMNPRV-Y])?)"\
                     r"|[0-9][A-HJKPS-UW]) ?[0-9][ABD-HJLNP-UW-Z]{2})$"

    # compile the regex
    VALID_POSTCODE_REGEX = re.compile(POSTCODE_REGEX)

    # Special cases and conditions

    # Areas with only one digit
    SINGLE_DIGIT_POSTAREA = ['BR', 'FY', 'HA', 'HD', 'HG', 'HR', 'HS', 'HX', 'JE', 'LD', 'SM', 'SR', 'WC', 'WN', 'ZE']

    # Areas with only two digit
    DOUBLE_DIGIT_POSTAREA = ['AB', 'LL', 'SO']

    # Areas with a zero district
    ZERO_DIGIT_POSTAREA = ['BL', 'BS', 'CM', 'CR', 'FY', 'HA', 'PR', 'SL', 'SS']

    # Central London - from wikipedia
    # The following central London single-digit districts have been further divided by inserting a letter after the
    # digit and before the space: EC1–EC4 (but not EC50), SW1, W1, WC1, WC2, and part of E1 (E1W), N1 (N1C and N1P),
    # NW1 (NW1W) and SE1 (SE1P).
    LETTER_FOLLOW = ['EC1', 'EC2', 'EC3' 'EC4', 'SW1', 'W1', 'WC1', 'WC2']

    # Special is_valid outward codes:
    # 1. although WC is always subdivided by a further letter, e.g. WC1A
    # 2. BS is the only area to have both a district 0 and a district 10
    # 3. part of E1 (E1W), N1 (N1C and N1P), NW1 (NW1W) and SE1 (SE1P)
    SPECIAL_COND_OUTWARD = ['WC1A', 'BS10', 'E1W', 'N1C', 'N1P', 'NW1W', 'SE1P']

    # Special invalid outward codes
    # The following central London single-digit districts have been further divided by inserting a letter after the
    # digit and before the space: EC1–EC4 (but not EC50), SW1, W1, WC1, WC2, and part of E1 (E1W), N1 (N1C and N1P),
    # NW1 (NW1W) and SE1 (SE1P).
    INVALID_OUTWARD = ['E1', 'N1', 'NW1', 'SE1', 'EC50']

    def __init__(self, in_postcode: str = "", fmt_postcode: str = "", outward_code: str = "", inward_code: str = "",
                 postcode_area: str = "", postcode_district: str = "", postcode_sector: str = "",
                 postcode_unit: str = "",
                 is_valid: bool = False, message: str = ""):
        """Postcode Constructor"""
        self.in_postcode = in_postcode
        self.fmt_postcode = fmt_postcode
        self.outward_code = outward_code
        self.inward_code = inward_code
        self.postcode_area = postcode_area
        self.postcode_district = postcode_district
        self.postcode_sector = postcode_sector
        self.postcode_unit = postcode_unit
        self.is_valid = is_valid
        self.message = ""

    def format(self, postcode: str) -> str:
        self.in_postcode = postcode
        """Format the post code and return the formatted value with inward and outward code
           
           Arguments
           postcode: string
        """
        # Check the length and return an error message if len is greater than 7 and less than 5
        if postcode is None:
            self.message = "ERROR: length must be minimum 5 and maximum 8"
            return self.message

        # Replace all the space
        postcode = postcode.replace(" ", "")

        if len(postcode) < 5 or len(postcode) > 7:
            self.message = "ERROR: length must be minimum 5 and maximum 8"
            return self.message

        # Throw error message if contains special characters
        if not postcode.isalnum():
            self.message = "ERROR: No special characters allowed"
            return self.message

        # Converting to upper case
        postcode = postcode.upper()
        # Extract the outward code except last 3
        self.outward_code = postcode[:-3]
        # Extract the inward code as last 3 chars
        self.inward_code = postcode[-3:]
        # Join outward and inward code
        self.fmt_postcode = self.outward_code + " " + self.inward_code
        self.message = "Formatted"

        return self.fmt_postcode

    def validate(self, postcode: str) -> bool:
        """Validate the given postcode string and return true if is valid

           Arguments
           Postcode: string
        """

        # Format the postcode
        self.format(postcode)

        # If the formatting of is successful
        if self.message == "Formatted":
            # Match the formatted postcode with the compliled regex
            if self.VALID_POSTCODE_REGEX.match(self.fmt_postcode):
                self.is_valid = True
                self.message = "VALID: the post code is valid"
            else:
                self.is_valid = False
                self.message = "INVALID: the post code is invalid"
            return self.is_valid

    def split_validate(self, postcode: str):
        """Validate, format and split the given code into separated components

           Arguments
           postcode: string
        """
        if self.validate(postcode):

            # Split the outward code on first digit to get area and district
            # Example outward code: NW1E; area: NW and district: 1E

            # Get the position of first digit
            district_start = re.search("\d", self.outward_code).start()
            # if contains a digit
            if district_start:
                # Get the area as all the characters before the first digit
                self.postcode_area = self.outward_code[:district_start]
                # Get the district as all the characters following the first digit
                self.postcode_district = self.outward_code[district_start:]

                # Check for special conditions
                if not (self.outward_code in self.SPECIAL_COND_OUTWARD):
                    if self.outward_code.startswith(tuple(self.LETTER_FOLLOW)):
                        if not self.postcode_district[-1:].isalpha():
                            self.message = "INVALID: the post code is invalid"
                            self.is_valid = False
                    elif self.postcode_area in self.DOUBLE_DIGIT_POSTAREA:
                        if len(self.postcode_district) != 2 or not (self.postcode_district.isdigit()):
                            self.message = "INVALID: the post code is invalid"
                            self.is_valid = False
                    elif self.postcode_area in self.SINGLE_DIGIT_POSTAREA:
                        if len(self.postcode_district) != 1 or not (self.postcode_district.isdigit()):
                            self.message = "INVALID: the post code is invalid"
                            self.is_valid = False

                    if self.outward_code.startswith(tuple(self.INVALID_OUTWARD)):
                        self.message = "INVALID: the post code is invalid"
                        self.is_valid = False

            if self.is_valid:
                # Split the inward code to get sector and unit

                # Get the sector from inward code as the first letter
                self.postcode_sector = self.inward_code[:1]
                # Get unit from inward code as the last 2 letters
                self.postcode_unit = self.inward_code[1:]
            else:
                self.postcode_area = ""
                self.postcode_district = ""