from telegram.ext import (
    Filters, Dispatcher, MessageHandler, CommandHandler
)

from .handlers.start import start_command_text
from .handlers.token import token_received
from .bot import bot

def setup_dispatcher(dp):
    dp.add_handler(CommandHandler("start", start_command_text))
    dp.add_handler(MessageHandler(Filters.all, token_received))
    return dp

dispatcher = setup_dispatcher(Dispatcher(bot, update_queue=None, workers=4, use_context=True))