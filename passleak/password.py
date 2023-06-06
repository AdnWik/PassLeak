import re


class Password:
    """Password abstract"""
    def __init__(self, password=None) -> None:
        self.password = password

    @property
    def password(self):
        """Password"""
        return self._password

    @password.setter
    def password(self, value):
        """Password"""
        password_tests_result = []

        password_tests_result.append(Password.check_length(value))

        if all(password_tests_result):
            password_tests_result.append(Password.check_digit(value))

        if all(password_tests_result):
            password_tests_result.append(Password.check_letters(value))

        if all(password_tests_result):
            password_tests_result.append(Password.check_special_char(value))

        if all(password_tests_result):
            self._password = value
        else:
            self._password = None

    @staticmethod
    def check_length(value: str, min_char=8) -> bool:
        """Check length of password

        Args:
            value (str): password
            min_char (int, optional): Minimum char amount in password.
                                      Defaults to 8.

        Returns:
            bool: Check result (True - OK , False - NOK)
        """

        try:
            if len(value) >= min_char:
                return True
            else:
                return False
        except TypeError:
            return False

    @staticmethod
    def check_digit(value: str) -> bool:
        """Check digit in password

        Args:
            value (str): password

        Returns:
            bool: Check result (True - OK , False - NOK)
        """

        if len(re.findall('[0-9]', value)) > 0:
            return True
        else:
            return False

    @staticmethod
    def check_letters(value: str) -> bool:
        """Check big and small letter in password

        Args:
            value (str): password

        Returns:
            bool: Check result (True - OK , False - NOK)
        """

        if len(re.findall('[A-Z]', value)) > 0:
            if len(re.findall('[a-z]', value)) > 0:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def check_special_char(value: str) -> bool:
        """Check special char in password

        Args:
            value (str): password

        Returns:
            bool: Check result (True - OK , False - NOK)
        """

        value_split = set(re.split('', value))
        value_no_special_char = set(re.findall('[a-zA-Z0-9_]', value))
        special_char = value_split.symmetric_difference(value_no_special_char)
        if len(special_char) > 1:
            return True
        else:
            return False
