from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "token",
        "text",
        "created_at"
    )

    list_filter = ("created_at",)

    fieldsets = (
        (
            "General",
            {
                "fields": (
                    "user",
                    "token",
                    "text",
                    "created_at"
                )
            },
        ),
    )