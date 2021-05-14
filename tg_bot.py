import telebot
import schedule
from threading import Thread
from telebot import types
from datetime import date, datetime
from time import sleep
from api import Cream
import os
#Enter API_KEY from file 'Keys'
API_KEY = '1886309037:AAE0jcZvgf1fuXJbokWmnyT40HFUElBzfzw'
bot = telebot.TeleBot(API_KEY)

markup_for_yes_no = types.InlineKeyboardMarkup()
item_yes = types.InlineKeyboardButton(text='YES', callback_data='yes')
item_no = types.InlineKeyboardButton(text='NO', callback_data='no')
markup_for_yes_no.add(item_yes, item_no)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hi! I`m a CosmeticsConsistension bot. I can analyze your cosmetic and give you some advice on it. To start -> send a command: /sendphoto")


@bot.message_handler(commands=['sendphoto'])
def add_photo(message):
    bot.send_message(message.chat.id, 'Please send a photo of your cosmetic ingredients.')
    bot.register_next_step_handler(message, photo)


@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'yes':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Here is your info')
        bot.send_message(call.message.chat.id, 'Fine. Thanks for using our service! To upload new photo -> /sendphoto\nSEE YOU LATER❤️')
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Fine. Thanks for using our service! To upload new photo -> /sendphoto\nSEE YOU LATER❤️')


def photo(message):
        try:
            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            lyst = Cream.find_ingredients(Cream(), downloaded_file)
            print(lyst)
            bot.reply_to(message, "Photo is being processed")
            bot.send_message(message.chat.id, "Do you want to get more info about ingredients?",
                reply_markup=markup_for_yes_no
            )
        except:
            bot.send_message(message.chat.id, "Invalid photo. To try again - send /sendphoto")


if __name__ == "__main__":
    bot.polling()
