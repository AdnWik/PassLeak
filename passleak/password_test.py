from password import Password


def password_test():
    value = '#123adcABC'

    score = Password(value)

    assert score.password == value
    assert score.power == None
    assert score.leaked == None
