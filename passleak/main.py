"""PassLeak main"""
import logging
from password_validator import PasswordValidator


logging.basicConfig(level=logging.INFO)

PasswordValidator.load_passwords()
PasswordValidator.validate()
PasswordValidator.validate_leaks()
logging.info(PasswordValidator.show_all_passwords())
PasswordValidator.save_safety_password()
