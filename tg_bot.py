import telebot
from telebot import types
from api import Cream
import os
from dataset_ADT import DataframeDataset

#Enter API_KEY from file 'Keys'
API_KEY = '1886309037:AAE0jcZvgf1fuXJbokWmnyT40HFUElBzfzw'
bot = telebot.TeleBot(API_KEY)

markup_for_yes_no = types.InlineKeyboardMarkup()
item_yes = types.InlineKeyboardButton(text='YES', callback_data='yes')
item_no = types.InlineKeyboardButton(text='NO', callback_data='no')
markup_for_yes_no.add(item_yes, item_no)
ingredients = None

cream_procesor = Cream()
forbidden_dataset = DataframeDataset()
description_dataset = DataframeDataset()
forbidden_dataset.read_data('x2_new.xlsx')
description_dataset.read_data('x_new.xlsx')

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
        global ingredients
        head = ingredients.next
        while head is not None:
            ingredient = head.element
            if ingredient is not None:
                diplay_ingredient = decorate_ingredient_display(ingredient)
                bot.send_message(call.message.chat.id, diplay_ingredient)

            head = head.next

        bot.send_message(call.message.chat.id, 'Fine. Thanks for using our service! To upload new photo -> /sendphoto\nSEE YOU LATER❤️')
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Fine. Thanks for using our service! To upload new photo -> /sendphoto\nSEE YOU LATER❤️')


def cut_spaces(string):
    string = string.split()
    string = ' '.join(string)
    return string

def decorate_ingredient_display(ingredient):
    strign = ''

    ingredient_name = ingredient['name']
    ingredient_assesment = ingredient['property0']
    ingredient_conclusion = cut_spaces(ingredient['property1'])

    ingredient_name_prefix = f'Detected ingredient: {ingredient_name}'
    safety_assesment_afix = f'Researches assesed with finding: {ingredient_assesment}'
    scientific_conclusion_sufix = f'Researche\'s conclusion: {ingredient_conclusion}'

    beaty_rafix = '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
    beaty_japix = '__________________________________________'
    beaty_gaxix = '------------------------------------------'

    text = f'{beaty_rafix}\n{ingredient_name_prefix}\n{beaty_gaxix}\n{safety_assesment_afix}\n{beaty_gaxix}\n{scientific_conclusion_sufix}\n{beaty_japix}' 

    return text

def photo(message):
        try:
            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            bot.reply_to(message, "Photo is being processed")
            global ingredients 
            ingredients = cream_procesor.check_ingredients(downloaded_file, description_dataset)

            forbiden_ingredients = cream_procesor.check_ingredients(downloaded_file, forbidden_dataset)
            head = forbiden_ingredients.next
            text = ''
            while head is not None:
                forbiden_ingredient = head.element
                if forbiden_ingredient:
                    text += str(forbiden_ingredient['name']) + '\n'
                head = head.next
            if text == '':
                bot.send_message(message.chat.id, 'There is no prohibited(dangerous) ingredients in this product')
            else:
                bot.send_message(message.chat.id, 'There are such prohibited(dangerous) ingredients in this product:\n' + text)
                
            bot.send_message(message.chat.id, "Do you want to get more info about ingredients?",
                reply_markup=markup_for_yes_no
            )
        except:
            bot.send_message(message.chat.id, "Invalid photo. To try again - send /sendphoto")

if __name__ == "__main__":
    bot.polling()