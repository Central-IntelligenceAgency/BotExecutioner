import telebot

from telebot import types
from admin import admin_connect, send_who_kill, handle_accept


def callback_query(bot: telebot.TeleBot, call: types.CallbackQuery):
    user_id = call.from_user.id

    if call.data == "KillOne":
        send_who_kill(bot, call.message, more_kill=True)

    elif call.data == "KillTwo":
        send_who_kill(bot, call.message, more_kill=False)

    elif call.data == "Accept":
        handle_accept(bot, call)

    elif call.data == "Exit":
        bot.delete_message(chat_id=call.message.chat_id, message_id=call.message.message_id)

    elif call.data == "Back":
        admin_connect(bot, call.message, user_id, edit=True)
