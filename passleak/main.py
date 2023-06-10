"""PassLeak main"""
from password_validator import PasswordValidator

PasswordValidator.load_passwords()
PasswordValidator.validate()
print(PasswordValidator.show_all_passwords())
