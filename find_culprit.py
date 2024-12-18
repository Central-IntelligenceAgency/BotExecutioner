import telebot
import random
import time

from config import users, users_white_list
from telebot import types


def find_user(kill_one=False):
    user_kill = random.choice(users)
    user_kill_2 = random.choice(users)
    users.remove(user_kill)
    print(f"Пользователь удолён {user_kill}")
    if kill_one:
        total_user = user_kill
    else:
        total_user = f"{user_kill} и {user_kill_2}"
    users_white_list.append(user_kill)
    print(f"В users_white_list добавлен {user_kill}")
    return total_user

