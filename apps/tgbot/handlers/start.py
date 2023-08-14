from telegram import Update
from telegram.ext import CallbackContext


def start_command_text(update: Update, context: CallbackContext) -> None:
    message = f'Привет, дорогой пользователь! Отправь мне сгенерированный токен и я автоматически произведу подключение!'
    update.message.reply_text(text=message)