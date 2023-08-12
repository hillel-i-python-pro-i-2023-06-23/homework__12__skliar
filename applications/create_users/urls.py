from django.urls import path
from . import views

apps_name = "create_users"

urlpatterns = [
    path("", views.create_users, name="create-users"),
]
