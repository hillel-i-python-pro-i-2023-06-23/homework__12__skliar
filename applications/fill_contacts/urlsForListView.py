from django.urls import path
from . import views
from . import views_ListView

apps_name = "test"

urlpatterns = [
    path("", views_ListView.UserList.as_view(), name="test"),
]
