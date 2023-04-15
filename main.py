from telebot import TeleBot
from telebot.types import Message
import config
from modules import crl

bot = TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message: Message):
    bot.send_message(message.chat.id, config.ABOUT_BOT_MESSAGE.format(message.from_user, bot.get_me()), parse_mode="html")


@bot.message_handler(commands=['check'])
def button_message(message: Message):
    """
    Главный метод, с которого начинается работы бота в crl.py класс CRLBaseChecker метод start
    :param message: Сообщение которое бот получает от пользователя для обработки ввода команд
    """
    chaecker1 = crl.CRLBaseChecker()
    bot.send_message(message.chat.id, chaecker1.start().format(message.from_user, bot.get_me()))


bot.polling(none_stop=True)