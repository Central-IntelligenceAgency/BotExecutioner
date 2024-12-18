import threading

import telebot

from admin import admin_connect
from clicking import callback_query
from config import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["admin"])
def send_welcome(message):
    user_id = message.from_user.id
    admin_connect(bot, message, user_id)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    threading.Thread(target=lambda: callback_query(bot, call)).start()


if __name__ == "__main__":
    bot.polling(non_stop=True)