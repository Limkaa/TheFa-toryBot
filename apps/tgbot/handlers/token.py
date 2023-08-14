from telegram import Update
from telegram.ext import CallbackContext

from apps.core.bot_tokens.models import UserBotToken


def token_received(update: Update, context: CallbackContext) -> None:
    token = UserBotToken.objects.filter(token=update.message.text).first()
    if token:
        token.chat_id = update.message.chat_id
        token.save()
        message = f'Отлично, чат подключен к системе, можно отправлять сообщения через REST API прямо в бота!'
    else:
        message = 'Упс! Такой токен не найден. Убедитесь, что токен введен верно'
    update.message.reply_text(text=message)