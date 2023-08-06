from .services.view_all_contacts import phoneuser_list
from .services.view_one_contact import view_one
from django.shortcuts import render

def all(request):
    return phoneuser_list(request)

def one_user(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        try:
            return view_one(request, user_id=user_id)
        except Exception as ex:
            error_message = "Пользователь с таким ID не найден."
            return render(request, "view_one.html", {"error_message": error_message})
    else:
        # Возвращаем HttpResponse для GET-запроса
        return render(request, "view_one.html")
