from django.contrib import admin
from .models import PhoneUser

# Register your models here.

# admin.site.register(PhoneUser)  #упрощоная реистрания


@admin.register(PhoneUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone_number",
        "date_create",
        "date_update",
    )

    list_filter = (
        "is_auto_generated",
        "date_create",
    )
