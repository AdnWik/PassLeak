"""Tests for PasswordValidator class"""
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
    """Length ok test"""

    value = 'Ab1#@!0c'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_length(password)

    score = password.power

    assert score == 1


def test_too_short_password():
    """Length nok test"""

    value = '!1cB'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_length(password)

    score = password.power

    assert score == 0


def test_digit_in_password():
    """Digit in password ok test"""

    value = 'abcd1ABCDEF!#*^'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_digit(password)

    score = password.power

    assert score == 1


def test_no_digit_in_password():
    """Digit in password nok test"""

    value = 'abcdABCDEF!#*^'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_digit(password)

    score = password.power

    assert score == 0


def test_small_letters_in_password():
    """Small letter in password ok test"""

    value = 'aABCDEF123!#*^'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_letters(password)

    score = password.power

    assert score == 1


def test_no_small_letters_in_password():
    """Small letter in password nok test"""

    value = 'ABCDEF123!#*^'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_letters(password)

    score = password.power

    assert score == 0


def test_big_letters_in_password():
    """Big letter in password ok test"""

    value = 'Babcdef123!#*^'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_letters(password)

    score = password.power

    assert score == 1


def test_no_big_letters_in_password():
    """Small letter in password nok test"""

    value = 'abcdef123!#*^'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_letters(password)

    score = password.power

    assert score == 0


def test_special_char_in_password():
    """Special character in password ok test"""

    value = '^abcdefABCD123'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_special_char(password)

    score = password.power

    assert score == 1


def test_no_special_char_in_password():
    """Special character in password ok test"""

    value = 'abcdefABCD123'
    password = Password(value)
    password.power = 0
    PasswordValidator.check_special_char(password)

    score = password.power

    assert score == 0


def test_ok_password_hash():
    # TODO:
    """A"""

    value = 'AbCdef12#$%'
    hash_value = 'a4f945c5f511c12831e135de2846fda16378ba3d'
    password = Password(value)
    password.power = 4
    PasswordValidator.hash_password(password)

    score = password.hash

    assert score == hash_value


def test_nok_password_hash():
    # TODO:
    """A"""

    value = 'abcdef12#$%'
    password = Password(value)
    password.power = 3
    PasswordValidator.hash_password(password)

    score = password.hash

    assert score is None


def test_ok_hash_request(requests_mock):
    # TODO:
    """TEST"""
    value = 'Z!mnaWod@1'
    password = Password(value)
    PasswordValidator.passwords.append(password)
    PasswordValidator.validate()
    hash_prefix = password.hash[:5]
    data = 'FEF38B22EE3082835F327AF955164AB06D3:4\nFEC7160D0224BE8279A13A7F582C757E4A9:1'
    url = 'https://api.pwnedpasswords.com/range/' + hash_prefix
    requests_mock.get(url, text=data)
    PasswordValidator.check_for_leaks(password)

    score = password.leaked

    assert score is False


def test_nok_hash_request(requests_mock):
    # TODO:
    """TEST"""
    value = 'Z!mnaWod@1'
    password = Password(value)
    PasswordValidator.passwords.append(password)
    PasswordValidator.validate()
    hash_prefix = password.hash[:5]
    hash_suffix = password.hash[5:].upper()
    data = f'FEF38B22EE3082835F327AF955164AB06D3:4\n{hash_suffix}:1'
    url = 'https://api.pwnedpasswords.com/range/' + hash_prefix
    requests_mock.get(url, text=data)
    PasswordValidator.check_for_leaks(password)

    score = password.leaked

    assert score is True
