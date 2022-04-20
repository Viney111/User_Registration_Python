"""
    @Author: Viney Khaneja
    @Date: 2022-04-20 11:05AM
    @Last Modified by: Viney Khaneja
    @Last Modified time: None
    @Title : Validating Class through Regex
"""

# Importing Regex Module
import re


class Regex_Validation:
    """
        Description: This Class having Functions to validate the user details
    """
    def validate_first_name(first_name):
        """
        Description: This function is to validate first name.
        Condition: Name should start with Capital letter and should have min 3 letters.
        Args: first_name: First name to validate
        Returns: Ture, if valid First name passed, Throws error and pass a message of Custom Exception
        """
        try:
            if re.match(r"^[A-Z]{1}[a-z]{2,}$", first_name):
                return True
            else:
                return False
        except Exception as ex:
            print(ex)
