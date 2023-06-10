from password import Password
from password_validator import PasswordValidator


def test_password_ok():
    """Good password test"""
    value = '#123adcABC^'
    password = Password(value)
    PasswordValidator.passwords.append(password)
    PasswordValidator.validate()

    score = password.power

    assert score == 4


def test_length_ok_password():
    #TODO: docstring
    value = 'Ab1#@!0c'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_length(password)

    score = password.power

    assert score == 1


def test_too_short_password():
    #TODO: docstring
    value = '!1cB'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_length(password)

    score = password.power

    assert score == 0


def test_digit_in_password():
    #TODO: docstring
    value = 'abcd1ABCDEF!#*^'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_digit(password)

    score = password.power

    assert score == 1


def test_no_digit_in_password():
    #TODO: docstring
    value = 'abcdABCDEF!#*^'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_digit(password)

    score = password.power

    assert score == 0


def test_small_letters_in_password():
    #TODO: docstring
    value = 'aABCDEF123!#*^'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_letters(password)

    score = password.power

    assert score == 1


def test_no_small_letters_in_password():
    #TODO: docstring
    value = 'ABCDEF123!#*^'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_letters(password)

    score = password.power

    assert score == 0


def test_big_letters_in_password():
    #TODO: docstring
    value = 'Babcdef123!#*^'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_letters(password)

    score = password.power

    assert score == 1


def test_no_big_letters_in_password():
    #TODO: docstring
    value = 'abcdef123!#*^'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_letters(password)

    score = password.power

    assert score == 0


def test_special_char_in_password():
    #TODO: docstring
    value = '^abcdefABCD123'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_special_char(password)

    score = password.power

    assert score == 1


def test_no_special_char_in_password():
    #TODO: docstring
    value = 'abcdefABCD123'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_special_char(password)

    score = password.power

    assert score == 0
