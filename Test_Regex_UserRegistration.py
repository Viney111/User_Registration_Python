"""
    @Author: Viney Khaneja
    @Date: 2022-04-20 10:41AM
    @Last Modified by: Viney Khaneja
    @Last Modified time: None
    @Title : Unit Test Class
"""

from Regex_Validation import Regex_Validation
import unittest


class Test_UserRegistration(unittest.TestCase):
    """
    Description: This class is to test all the methods used in addressBook
    """

    def test_first_name_when_entered_correct_should_return_true(self):
        """
            Description: Unit Test to verify first Name positively
            Parametres: Takes correct first name
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertTrue(Regex_Validation.validate_first_name("Viney"))
        self.assertTrue(Regex_Validation.validate_first_name("Vishal"))

    def test_first_name_when_entered_incorrect_should_return_false(self):
        """
            Description: Unit Test to verify first Name negatively
            Parametres: Takes Incorrect first name
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertFalse(Regex_Validation.validate_first_name("viney"))
        self.assertFalse(Regex_Validation.validate_first_name("Vi"))

    def test_last_name_when_entered_correct_should_return_true(self):
        """
            Description: Unit Test to verify last Name positively
            Parametres: Takes correct last name
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertTrue(Regex_Validation.validate_last_name("Khaneja"))
        self.assertTrue(Regex_Validation.validate_last_name("Juneja"))

    def test_last_name_when_entered_incorrect_should_return_false(self):
        """
            Description: Unit Test to verify last Name negatively
            Parametres: Takes Incorrect last name
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertFalse(Regex_Validation.validate_last_name("Kj"))
        self.assertFalse(Regex_Validation.validate_last_name("juneja"))
