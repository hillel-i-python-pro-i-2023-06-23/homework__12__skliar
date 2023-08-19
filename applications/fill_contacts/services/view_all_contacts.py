from applications.fill_contacts.models import PhoneUser

# from django.shortcuts import render


def phoneuser_list():
    phoneusers = PhoneUser.objects.all()
    return phoneusers
