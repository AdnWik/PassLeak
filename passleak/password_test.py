"""Password class tests"""

from password import Password


def password_test():
    """Password object create test"""

    value = '#123adcABC'

    score = Password(value)

    assert score.password == value
    assert score.power is None
    assert score.leaked is None
    assert score.hash is None
