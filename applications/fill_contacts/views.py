from applications.fill_contacts.models import PhoneUser
from django.shortcuts import render
from django.views.generic import ListView


def phoneuser_list(request):
    phoneusers = PhoneUser.objects.all()
    return render(request, "phoneuser_list.html", {"phoneusers": phoneusers})


class UserList(ListView):
    model = PhoneUser
    template_name = "forListView.html"
