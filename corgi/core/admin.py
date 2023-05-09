from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as CorgiUserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(CorgiUserAdmin):
    add_fieldsets = (
        (
        None,
        {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2", "email", "first_name",
                       "last_name", "phone", "address")
        },
        ),
    )
    list_display = ("username", "email", "first_name", "last_name", "phone")