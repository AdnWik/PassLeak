"""Password class"""


class Password:
    """Password abstract"""
    def __init__(self, password) -> None:
        self.password = password
        self.power = None
        self.leaked = None

    def __repr__(self) -> str:
        return (f'Password: {self.password} Power: {self.power}'
                f' Leaked: {self.leaked}')

    def __str__(self) -> str:
        return (f'Password: {self.password:<20} Power: {self.power}'
                f'  Leaked: {self.leaked}')
