from django.shortcuts import get_object_or_404, render
from applications.fill_contacts.models import PhoneUser


def view_one(request, user_id):
    phoneuser = get_object_or_404(PhoneUser, id=user_id)
    return render(request, "view_one.html", {"phoneuser": phoneuser})
