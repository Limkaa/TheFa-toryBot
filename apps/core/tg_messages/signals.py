from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import BadRequest

from rest_framework.response import Response

from .models import Message

from apps.tgbot.utils import send_one_message

MESSAGE_TEMPLATE = "{name}, я получил от тебя сообщение:\n{message}"

@receiver(post_save, sender=Message)
def send_message_to_telegram(sender, instance: Message, created, **kwargs):
    if created:
        message = MESSAGE_TEMPLATE.format(
            name=instance.user.first_name,
            message=instance.text,
        )

        if instance.token.chat_id:
            send_one_message(instance.token.chat_id, message)