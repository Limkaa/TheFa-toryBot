import binascii, os

from django.db import models
from django.db.models import manager

from ..users.models import User


class UserBotToken(models.Model):
    ''' Represents user tokens for connecting to telegram bot '''
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, null=False)
    token = models.CharField(max_length=100, blank=False, null=False, unique=True)
    chat_id = models.CharField(max_length=30, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_token()
        return super(UserBotToken, self).save(*args, **kwargs)

    def generate_token(self):
        return binascii.hexlify(os.urandom(20)).decode()
    
    def __str__(self) -> str:
        return self.token