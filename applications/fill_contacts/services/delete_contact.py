from django.shortcuts import render, get_object_or_404
from applications.fill_contacts.models import PhoneUser

def delete_user(request, user_id):
    phoneuser = get_object_or_404(PhoneUser, id=user_id)
    phoneuser.delete()
    return render(request, "delete_user.html", {"phoneuser": phoneuser})
