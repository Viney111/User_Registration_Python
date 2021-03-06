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
        Returns: True, if valid input given..False, if invalid input given
        """
        try:
            if re.match(r"^[A-Z]{1}[a-z]{2,}$", first_name):
                return True
            else:
                return False
        except Exception as ex:
            print(ex)

    def validate_last_name(last_name):
        """
        Description: This function is to validate last name.
        Condition: Name should start with Capital letter and should have min 3 letters.
        Args: last_name: Last name to validate
        Returns: True, if valid input given..False, if invalid input given
        """
        try:
            if re.match(r"^[A-Z]{1}[a-z]{2,}$", last_name):
                return True
            else:
                return False
        except Exception as ex:
            print(ex)

    def validate_email(email):
        """
        Description: This function is to validate email.
        Condition: Email should contain @ and . and other conditions
        Args: email: To be validated
        Returns: True, if valid input given..False, if invalid input given
        """
        try:
            if re.match(r"^[0-9a-z]+[+_.-]?[0-9a-z]+[@][0-9a-z]+[.][a-z]{2,}[.]?[a-z]+$", email):
                return True
            else:
                return False
        except Exception as ex:
            print(ex)

    def validate_phone_number(phone_number):
        """
        Description: This function is to validate phone number.
        Condition: Phone number should start with 91 and should have space afer that, followed by 10 numerical values
        Args: phone_number: To be validated
        Returns: True, if valid input given..False, if invalid input given
        """
        try:
            if re.match(r"^[0-9]{2}[ ][6-9]{1}[0-9]{9}$", phone_number):
                return True
            else:
                return False
        except Exception as ex:
            print(ex)

    def validate_password(password):
        """
        Description: This function is to validate password.
        Condition: Password should contain min 8 characters,at least one uppercase,at least one lowercase & one special character.
        Args: password: To be validated
        Returns: True, if valid input given..False, if invalid input given
        """
        try:
            if re.match(r"^(?=.*[!@#$%^&*])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z1-9]{1}[a-zA-Z0-9]{7,}", password):
                return True
            else:
                return False
        except Exception as ex:
            print(ex)
