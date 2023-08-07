"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include

# from applications.base import views as base_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", include("applications.base.urls")),
    path("create-users/", include("applications.create_users.urls")),
    path("phoneuser/", include("applications.fill_contacts.urls")),
    path("test/", include("applications.fill_contacts.urls")),
    path("all/", include("applications.fill_contacts.urls")),
    path("one/", include("applications.fill_contacts.urls")),
    path("add/", include("applications.fill_contacts.urls")),
    path("delete/", include("applications.fill_contacts.urls")),
    path("update/", include("applications.fill_contacts.urls")),
]
