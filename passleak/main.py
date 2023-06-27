"""PassLeak main"""
import logging
from password_validators.validators import PasswordValidator, ValidatorError

logging.basicConfig(level=logging.INFO)

URL = 'passleak/'

try:
    with (open(URL + 'passwords.txt', encoding='UTF-8')as input_file,
          open(URL + 'safety.txt', 'w', encoding='UTF-8') as output_file):
        for password in input_file:
            try:
                validator = PasswordValidator(password.rstrip('\n'))
                validator.is_valid()
                output_file.write(password)
            except ValidatorError as error:
                print(error)
except FileNotFoundError:
    with (open(URL + 'passwords.txt', 'w')):
        print('Write passwords to passwords.txt')
