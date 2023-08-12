from django.urls import path
from . import views


apps_name = "fill_contacts"

urlpatterns = [
    path("", views.phoneuser_list, name="phone-user-list"),
]
