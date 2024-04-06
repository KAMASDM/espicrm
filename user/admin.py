
from typing import Any

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.created_by = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(CustomUser, UserAdmin)
