"""PassLeak main"""
from password_validator import PasswordValidator

PasswordValidator.load_passwords()
PasswordValidator.validate()
PasswordValidator.validate_leaks()
print(PasswordValidator.show_all_passwords())
PasswordValidator.save_safety_password()
