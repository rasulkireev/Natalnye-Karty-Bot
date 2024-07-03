import os

import telebot
from dotenv import load_dotenv

from natalnye_karty_bot.utils import get_natal_map

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'привет'])
def send_welcome(message):
    bot.reply_to(message, "Привет, как дела?")


@bot.message_handler(commands=['create', 'создать'])
def name_handler(message):
    text = "Как вас зовут? Полное имя пожалуйста, например 'Иван Иванов'"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, birth_date_handler)


def birth_date_handler(message):
    name = message.text
    text = "Когда вы родились? Введите дату в формате ДД/ММ/ГГГГ"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, birth_time_handler, name)


def birth_time_handler(message, name):
    birth_date = message.text
    text = "Введите время рождения в формате ЧЧ:ММ"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, birth_location_handler, name, birth_date)


def birth_location_handler(message, name, birth_date):
    birth_time = message.text
    text = "Введите место рождения (Город, Страна)"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, fetch_natal_map, name, birth_date, birth_time)


def fetch_natal_map(message, name, birth_date, birth_time):
    birth_location = message.text
    map = get_natal_map(name, birth_date, birth_time, birth_location)
    bot.send_message(message.chat.id, "Ваша карта готова!")
    bot.send_message(message.chat.id, map, parse_mode="Markdown")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
