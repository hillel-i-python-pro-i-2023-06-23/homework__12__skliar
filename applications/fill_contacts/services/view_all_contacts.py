from applications.fill_contacts.models import PhoneUser
from django.shortcuts import render


def phoneuser_list(request):
    phoneusers = PhoneUser.objects.all()
    return render(request, "view_all.html", {"phoneusers": phoneusers})
