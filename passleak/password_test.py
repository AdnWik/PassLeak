from password import Password


def test_password_values_ok():
    """Good password test"""
    value = '#123adcABC'

    score = Password(value)

    assert score.password == value


def test_password_values_nok():
    """Wrong password test"""
    value_nok = 'password'

    score_none = Password()
    score_nok = Password(value_nok)

    assert score_none.password is None
    assert score_nok.password is None
