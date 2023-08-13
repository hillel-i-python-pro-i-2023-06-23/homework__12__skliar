import re


class UserData:
    def __init__(self, login=None, email=None, password=None):
        self.login = self._validate_login(login)
        self.email = self._validate_email(email)
        self.password = UserData._validate_password(password)

    def _validate_login(self, login):
        if login is None:
            raise ValueError("Логин не может быть пустым.")
        if not re.match(r"^[a-zA-Z0-9_]*$", login):
            raise ValueError(
                "Логин должен содержать только латинские буквы, цифры и символ подчеркивания.",
            )
        return login

    #
    def _validate_email(self, email):
        if email is None:
            raise ValueError("Адрес электронной почты не может быть пустым.")

        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            raise ValueError("Некорректный адрес электронной почты.")
        return email

    @classmethod
    def _validate_password(cls, password):
        if password is None:
            raise ValueError("Пароль не может быть пустым.")
        if len(password) < 8:
            raise ValueError("Минимум 8 символов.")
        if not any(char.isupper() for char in password):
            raise ValueError("Минимум одна заглавная буква.")
        if not any(char.isdigit() for char in password):
            raise ValueError("Минимум одна цифра.")
        special_chars = r"[#$%!_*&]"
        if not re.search(special_chars, password):
            raise ValueError("Минимум один специальный символ: #$%!_*&")
        return password

    def __str__(self):
        return f"Username: {self.login}, Email: {self.email}, Password: {self.password}"
