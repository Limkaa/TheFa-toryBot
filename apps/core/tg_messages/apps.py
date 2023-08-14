from django.apps import AppConfig


class MessagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core.tg_messages'
    
    def ready(self) -> None:
        from . import signals
