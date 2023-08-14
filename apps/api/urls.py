from django.urls import include, path

urlpatterns = [
    path("auth-token/", include(("apps.authentication.urls", "authentication"))),
    path("users/", include(("apps.core.users.urls", "users"))),
    path("bot-token", include(("apps.core.bot_tokens.urls", "tokens"))),
    path("messages", include(("apps.core.tg_messages.urls", "messages"))),
]
