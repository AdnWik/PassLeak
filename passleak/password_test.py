from password import Password


def test_password_values():
    """Password different type of values test"""
    value_int = 1
    value_str = 'TEST'

    score_none = Password()
    score_int = Password(value_int)
    score_str = Password(value_str)

    assert score_none.password is None
    assert score_int.password is None
    assert score_str.password == value_str
