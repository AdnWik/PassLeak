from password import Password


class Verifier:

    def __init__(self) -> None:
        self.passwords = []

        with open('passwords.txt', 'r', encoding='utf-8') as file:
            _passwords = file.read().split('\n')

        for password in _passwords:
            self.passwords.append(Password(password))

v1 = Verifier()
for _ in v1.passwords:
    print(_.password)
