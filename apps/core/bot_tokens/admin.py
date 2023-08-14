from django.contrib import admin

from .models import UserBotToken


@admin.register(UserBotToken)
class UserBotTokenAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "token",
        "chat_id",
    )

    search_fields = ("token", "chat_id")

    fieldsets = (
        (
            "General",
            {
                "fields": (
                    "user",
                    "token",
                    "chat_id",
                )
            },
        ),
    )
