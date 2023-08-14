from django.db import models

from ..users.models import User
from ..bot_tokens.models import UserBotToken


class Message(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False, blank=False)
    token = models.ForeignKey(to=UserBotToken, on_delete=models.CASCADE, null=False, blank=False)
    text = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.text
    