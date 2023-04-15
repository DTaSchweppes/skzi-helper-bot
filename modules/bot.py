from telebot import TeleBot
from telebot import types
from telebot.types import Message
import config
from modules import crl

bot = TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message: Message):
    bot.send_message(message.chat.id, "Старт".format(message.from_user, bot.get_me()), parse_mode="html")


@bot.message_handler(commands=['check'])
def button_message(message : Message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    butt_check_crl=types.KeyboardButton("check")
    markup.add(butt_check_crl)
    chaecker1 = crl.CRLBaseChecker()
    bot.send_message(message.chat.id, chaecker1.start().format(message.from_user, bot.get_me()), reply_markup=markup)


bot.polling(none_stop=True)