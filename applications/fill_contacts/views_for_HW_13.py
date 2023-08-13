# from django.core.exceptions import ObjectDoesNotExist
from .services.view_all_contacts import phoneuser_list
from .services.view_one_contact import view_one
from .services.add_contact import add_phone_user
from .services.delete_contact import delete_user
from django.shortcuts import render
from .services.update_contact import update_user


def all(request):
    return phoneuser_list(request)


def one_user(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        try:
            return view_one(request, user_id=user_id)
        except Exception:
            error_message = "Пользователь с таким ID не найден."
            return render(request, "view_one.html", {"error_message": error_message})
    else:
        # Возвращаем HttpResponse для GET-запроса
        return render(request, "view_one.html")


def add_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone_number = request.POST.get("tel_num")
        try:
            add_phone_user(name, phone_number)
            message = "Добавлен"
            return render(request, "add_user.html", {"message": message})
        except Exception:
            message = "НЕ добавлен"
            return render(request, "add_user.html", {"message": message})
    else:
        return render(request, "add_user.html")


def delete(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        try:
            delete_user(request, user_id=user_id)
            message = "Удален"
            return render(request, "delete_user.html", {"message": message})
        except Exception:
            message = "Пользователь с таким ID не найден."
            return render(request, "delete_user.html", {"message": message})
    else:
        # Возвращаем HttpResponse для GET-запроса
        return render(request, "delete_user.html")


def update(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        new_name = request.POST.get("name")
        new_number = request.POST.get("tel_num")
        try:
            update_user(request, user_id, new_name, new_number)
            message = "Изменен"
            return render(request, "update_user.html", {"message": message})
        except Exception:
            message = "НЕ изменен"
            return render(request, "update_user.html", {"message": message})
    else:
        return render(request, "update_user.html")
