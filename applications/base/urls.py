from django.urls import path
from . import views

apps_name = "base"

urlpatterns = [
    path("", views.index, name="home"),
]
