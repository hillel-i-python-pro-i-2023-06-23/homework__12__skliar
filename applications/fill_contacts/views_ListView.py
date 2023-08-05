from applications.fill_contacts.models import PhoneUser
from django.shortcuts import render
from django.views.generic import ListView


class UserList(ListView):
    model = PhoneUser
    template_name = "forListView.html"