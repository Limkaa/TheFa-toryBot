from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "first_name",
        "is_active",
        "date_joined",
    )

    search_fields = ("email", "first_name")

    list_filter = ("is_active", "is_staff", "is_superuser")

    fieldsets = (
        (
            "General",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                )
            },
        ),
        ("Booleans", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Timestamps", {"fields": ("date_joined",)}),
    )

    readonly_fields = ("date_joined",)
