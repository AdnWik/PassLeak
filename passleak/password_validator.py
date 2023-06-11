"""Verifier class"""
from abc import ABC, abstractmethod
import re
from hashlib import sha1
from requests import get
from password import Password


class PasswordValidatorInterface(ABC):
    """Password validator interface"""

    @abstractmethod
    def validate():
        """Validate method"""


class PasswordValidator(PasswordValidatorInterface):
    """Verifier abstract"""

    passwords = []

    @classmethod
    def load_passwords(cls) -> None:
        """Load passwords from passwords.txt"""

        with open('passwords.txt', 'r', encoding='utf-8') as file:
            for password in file.read().split('\n'):
                cls.passwords.append(Password(password))

    @classmethod
    def validate(cls) -> None:
        """Verification of password requirements and leaks """

        for password in cls.passwords:
            password.power = 0
            cls.check_length(password)
            cls.check_digit(password)
            cls.check_letters(password)
            cls.check_special_char(password)
            cls.hash_password(password)
            cls.check_for_leaks(password)

    @classmethod
    def show_all_passwords(cls) -> str:
        """Show all loaded passwords"""

        message = ''
        for password in cls.passwords:
            message += f'{password}\n'
        return message

    @staticmethod
    def check_length(password: object, min_char=8) -> None:
        """Verification of the number of characters"""

        if len(password.password) >= min_char:
            password.power += 1

    @staticmethod
    def check_digit(password: object) -> None:
        """Verifying the presence of a digit"""

        if len(re.findall('[0-9]', password.password)) > 0:
            password.power += 1

    @staticmethod
    def check_letters(password: object) -> None:
        """verifying the presence
           of upper and lower case letters"""

        if len(re.findall('[A-Z]', password.password)) > 0:
            if len(re.findall('[a-z]', password.password)) > 0:
                password.power += 1

    @staticmethod
    def check_special_char(password: object) -> None:
        """verification of the presence
           of a special character"""

        value_split = set(re.split('', password.password))
        value_no_special_char = set(
            re.findall('[a-zA-Z0-9_]', password.password))

        special_char = value_split.symmetric_difference(value_no_special_char)
        if len(special_char) > 1:
            password.power += 1

    @staticmethod
    def hash_password(password: object) -> None:
        """Create password hash"""
        if password.power == 4:
            h = sha1()
            h.update(password.password.encode(encoding='UTF-8'))
            password.hash = h.hexdigest()

    #TODO:
    @staticmethod
    def check_for_leaks(password: object) -> None:
        """Check password in haveibeenpawned.com"""
        if password.hash is not None:
            _hash_first_five = password.hash[:5]
            url = 'https://api.pwnedpasswords.com/range/' + _hash_first_five
            with get(url) as content:
                    hash_list = [tuple(row.split(':'))
                           for row in content.text.splitlines()]
            for hash, leaked in hash_list:
                    
                    print('\n')
                    print(f'{hash} | {leaked}')
                    print(f'{password.hash[:5:-1].upper()}')

