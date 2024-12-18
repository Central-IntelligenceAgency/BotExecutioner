import telebot
import time

from telebot import types
from config import admin
from find_culprit import find_user
from config import allowed_channels


def admin_kb_menu():
    keyboard = types.InlineKeyboardMarkup()

    btn_kill_one = types.InlineKeyboardButton(text="Казнить одного", callback_data="KillOne")
    btn_kill_two = types.InlineKeyboardButton(text="Канзнить двоих", callback_data="KillTwo")
    btn_exit = types.InlineKeyboardButton(text="Выйти", callback_data="Exit")

    keyboard.add(btn_kill_one)
    keyboard.add(btn_kill_two)
    keyboard.add(btn_exit)

    return keyboard


def is_user_admin(user_id):
    return user_id in admin


def admin_connect(bot: telebot.TeleBot, message: types.Message, user_id, edit=False):
    if not is_user_admin(user_id):
        bot.send_message(message.chat.id, "Я тебя не знаю!")
        return

    user_name = admin[user_id]

    keyboard = admin_kb_menu()
    if not edit:
        bot.send_message(message.chat.id, "Жду приказов:", reply_markup=keyboard)
    else:
        bot.edit_message_text(
            text="Жду приказов сер",
            chat_id=message.chat.id,
            message_id=message.message_id,
            reply_markup=keyboard
        )


def accept_menu():
    kb_accept = types.InlineKeyboardMarkup()

    btn_accept = types.InlineKeyboardButton(text="Подтврердить", callback_data="Accept")
    btn_back = types.InlineKeyboardButton(text="Назад", callback_data="Back")

    kb_accept.add(btn_accept)
    kb_accept.add(btn_back)

    return kb_accept


def logic(more_kill=False):
    return find_user(kill_one=more_kill)


def send_who_kill(bot: telebot.TeleBot, message: types.Message, more_kill=False):
    total_user = logic(more_kill)
    keyboard = accept_menu()
    bot.edit_message_text(
        f"Подтвердите, что должны дежурить: {total_user}",
        chat_id=message.chat.id,
        message_id=message.message_id,
        reply_markup=keyboard
    )


def send_total(bot: telebot.TeleBot, total_user):
    bot.send_message(allowed_channels, "Верховным судом Прогеймов, имени императора Z...")
    time.sleep(2)
    bot.send_message(allowed_channels, "К высшей мере исполнительной власти приговаривается")
    time.sleep(2)
    bot.send_message(allowed_channels, total_user)


def handle_accept(bot, call: types.CallbackQuery):
    total_user = call.message.text.split(": ")[1]
    send_total(bot, total_user)





