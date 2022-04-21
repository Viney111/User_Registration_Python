"""
    @Author: Viney Khaneja
    @Date: 2022-04-20 12:41AM
    @Last Modified by: Viney Khaneja
    @Last Modified time: None
    @Title : Py Test Class
"""

from Regex_Validation import Regex_Validation
import json


with open('ValidData.json') as read_valid_json:
    valid_data = json.load(read_valid_json)

    def test_validFirstName():
        """
        Description: 
            In this test case when given a valid first name should return true.
        """

        for user in valid_data:
            f_name = user['firstName']
            assert Regex_Validation.validate_first_name(f_name) == True

    def test_validLastName():
        """
        Description: 
            In this test case when given a valid last name should return true.
        """

        for user in valid_data:
            l_name = user['lastName']
            assert Regex_Validation.validate_last_name(l_name) == True

    def test_validMobileNumber():
        """
        Description: 
            In this test case when given a valid mobile number should return true.
        """

        for user in valid_data:
            phone_no = user['mobile']
            assert Regex_Validation.validate_phone_number(phone_no) == True

    def test_validPassword():
        """
        Description: 
            In this test case when given a valid password should return true.
        """

        for user in valid_data:
            passcode = user['password']
            assert Regex_Validation.validate_password(passcode) == True

    def test_validEmail():
        """
        Description: 
            In this test case when given a valid email should return true.
        """

        for user in valid_data:
            mail = user['email']
            assert Regex_Validation.validate_email(mail) == True

with open('InvalidData.json') as read_invalid_json:
    invalid_data = json.load(read_invalid_json)

    def test_invalidFirstName():
        """
        Description: In this test case when given a invalid first name should return false.
        """
        for user in invalid_data:
            f_name = user['firstName']
            assert Regex_Validation.validate_first_name(f_name) == False

    def test_invalidLastName():
        """
        Description: 
            In this test case when given a invalid last name should return false.
        """

        for user in invalid_data:
            l_name = user['lastName']
            assert Regex_Validation.validate_last_name(l_name) == False

    def test_invalidMobileNumber():
        """
        Description: 
            In this test case when given a invalid mobile number should return false.
        """

        for user in invalid_data:
            phone_no = user['mobile']
            assert Regex_Validation.validate_phone_number(phone_no) == False

    def test_invalidPassword():
        """
        Description: 
            In this test case when given a invalid password should return false.
        """
        for user in invalid_data:
            passcode = user['password']
            assert Regex_Validation.validate_password(passcode) == False

    def test_invalidEmail():
        """
        Description: 
            In this test case when given a invalid email should return false.
        """

        for user in invalid_data:
            mail = user['email']
            assert Regex_Validation.validate_email(mail) == False
