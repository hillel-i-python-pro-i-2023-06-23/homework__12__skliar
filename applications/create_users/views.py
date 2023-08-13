from typing import List
from faker import Faker
from django.shortcuts import render
from applications.create_users.services.init_user import UserData
from applications.create_users.services.generate_password import generate_password

# Create your views here.


def create_users(request):
    if request.method == "POST":
        num_users_str = request.POST.get("num_users")
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
        return render(
            request,
            template_name="create_users.html",
        )
