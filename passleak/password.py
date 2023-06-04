"""Class password"""


class Password:
    """Password abstract"""
    def __init__(self, password=None) -> None:
        self.password = password

    @property
    def password(self):
        """Password"""
        return self._password

    @password.setter
    def password(self, value):
        """Password"""
        if isinstance(value, str):
            self._password = value
        else:
            self._password = None