import string
import random
from typing import List
from faker import Faker

from django.shortcuts import render
from django.http import HttpResponseNotAllowed
import re

# Create your views here.


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


def generate_password():
    characters = string.ascii_letters + string.digits + r"#$%!_*&"
    while True:
        length = random.randint(8, 20)
        password = "".join(random.choice(characters) for _ in range(length))
        try:
            UserData._validate_password(password)
            print(f"ok {password}")
            return password
        except ValueError as e:
            print(f"no {password} {e}")
            # Если пароль не проходит валидацию, генерируем новый пароль
            continue
    return password


def create_users(request):
    if request.method == "POST" or request.method == "GET":
        num_users_str = request.GET.get("num_users")
        if num_users_str is not None and num_users_str.isdigit():
            kol_users = int(num_users_str)
        else:
            kol_users = 0

        users_data: List[UserData] = []

        for _ in range(kol_users):
            login = Faker().user_name()
            email = f"{login}@ex.com"
            password = generate_password()

            user = UserData(login=login, email=email, password=password)
            users_data.append(user)

        context = {"users_data": users_data}  # Передаем список пользователей в контекст
        return render(
            request=request,
            template_name="create_users.html",
            context=context,
        )
    else:
        return HttpResponseNotAllowed(["POST"])
