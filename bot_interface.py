'''
Telegram Bot Interface.
'''

# Import the needed libraries
import telebot
from telebot import types
from vision_api import Cream
from dataset_ADT import DataframeDataset

# Enter API_KEY from file 'Keys'
ingredients = None
API_KEY = '1886309037:AAE0jcZvgf1fuXJbokWmnyT40HFUElBzfzw'

# Create and activate bot-service instanec.
bot = telebot.TeleBot(API_KEY)

# Markups for the interface.
markup_for_yes_no = types.InlineKeyboardMarkup()

item_yes = types.InlineKeyboardButton(text='YES', callback_data='yes')
item_no = types.InlineKeyboardButton(text='NO', callback_data='no')

markup_for_yes_no.add(item_yes, item_no)

picture = open('examples/template.jpg', 'rb')

# Create a 'Cream' ADT-service instance.
cream_procesor = Cream()

# Create storage-service ADTs for the datasets.
forbidden_dataset = DataframeDataset()
description_dataset = DataframeDataset()

# Store the datasets.
forbidden_dataset.read_data('datasets/dataset_forbidden.xlsx')
description_dataset.read_data('datasets/dataset_ingredients.xlsx')

# Handle the initial message.


@bot.message_handler(commands=['start'])
def start(message):
    """
    Start the dialofg with the bot.

    Args:
        message ([telebot.types.Message]): [message interface-service].
    """
    bot.send_photo(message.chat.id, picture)
    bot.send_message(message.chat.id, "Hi! I`m a message.chat.idmessage.chat.id bot. \
I can analyze your cosmetics and give you some advice on it. To start -> send a command: /sendphoto")


# Handle the sending communication-message process.
@bot.message_handler(commands=['sendphoto'])
def add_photo(message):
    """
    Receives a photo from the user.

    Args:
        message ([telebot.types.Message]): [message with user's photo].
    """
    bot.send_message(
        message.chat.id, 'Please send a photo of your cosmetic ingredients.')

    # Activate the handler of the new messages.
    bot.register_next_step_handler(message, photo)


# Handler for the answering-dialog interface.
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    """
    Programs the 'Yes'-'No' answer interface.

    Args:
        call ([telebot.types.Message]): [call-answer from the user].
    """
    # Access global ingredients storage-variable.
    global ingredients

    # 'Yes' condition.
    present_hazards = False
    if call.data == 'yes':
        # Delete the message to clean the chat.
        bot.delete_message(call.message.chat.id, call.message.message_id)

        # Loop over the linked-list with ingredients.
        head = ingredients.next
        while head is not None:
            ingredient = head.element

            # If the ingredient has been found send the info about and send the reply.
            if ingredient is not None:
                present_hazards = True
                diplay_ingredient = decorate_ingredient_display(ingredient)
                bot.send_message(call.message.chat.id, diplay_ingredient)

            head = head.next

        if not present_hazards:
            bot.send_message(
                call.message.chat.id, 'We weren\'t able to find more info about the ingredients in your products.')

    bot.send_message(call.message.chat.id,
                     'Thanks for using our service! To upload a new photo -> /sendphoto\nSEE YOU LATER❤️')


def cut_spaces(string):
    """
    Cleans the given string of the redundant spaces.

    Args:
        string ([str]): [a string to clean].

    Returns:
        [str]: [a cleaned of the redundant spaces string].
    """
    string = string.split()
    string = ' '.join(string)

    return string


def decorate_ingredient_display(ingredient):
    """
    Decorator for the messages.

    Args:
        ingredient ([dictionary]): [a dictionary describing an ingredient].

    Returns:
        [string]: [a decorated string representing the ingredient].
    """
    # Retrieve the data about the ingredient.
    ingredient_name = ingredient['name']
    ingredient_assesment = ingredient['property0']
    ingredient_conclusion = cut_spaces(ingredient['property1'])

    # Create segments of the decorated string.
    ingredient_name_prefix = f'Detected ingredient: {ingredient_name}'
    safety_assesment_afix = f'Researches assesed with finding: {ingredient_assesment}'
    scientific_conclusion_sufix = f'Researche\'s conclusion: {ingredient_conclusion}'

    # Helping string-decorators.
    beaty_rafix = '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
    beaty_japix = '__________________________________________'
    beaty_gaxix = '------------------------------------------'

    # The final string.
    text = f'{beaty_rafix}\n{ingredient_name_prefix}\n{beaty_gaxix}\n\
{safety_assesment_afix}\n{beaty_gaxix}\n{scientific_conclusion_sufix}\n{beaty_japix}'

    return text


def photo(message):
    """
    Receive a photo from a user.

    Args:
        message ([telebot.types.Message]): [message with a photo].
    """
    # Access global ingredients storage-variable.
    global ingredients
    try:
        text = ''

        # Retrieve the info abotu the file.
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)

        # Reetrive the file receive from the user.
        photo_file = bot.download_file(file_info.file_path)

        bot.reply_to(message, "Photo is being processed...")

        # Retrive the info on the ingredients on the photo from the ingredients dataset.
        ingredients = cream_procesor.check_ingredients(
            photo_file, description_dataset)

        # Retrive the info on the ingredients on the photo from the dataset of prohibitions.
        forbiden_ingredients = cream_procesor.check_ingredients(
            photo_file, forbidden_dataset)

        head = forbiden_ingredients.next

        # Loop over the linked-list with ingredients.
        while head is not None:
            forbiden_ingredient = head.element
            if forbiden_ingredient is not None:
                text += str(forbiden_ingredient['name']) + '\n' + \
                    '---------------------------------' + '\n'

            head = head.next

        if text == '':
            bot.send_message(
                message.chat.id, 'There is no prohibited (dangerous) ingredients in this product')

        else:
            bot.send_message(
                message.chat.id, 'There are such prohibited (dangerous) ingredients in this product:\n' + text)

        bot.send_message(message.chat.id, "Do you want to get more info about ingredients?",
                         reply_markup=markup_for_yes_no
                         )

    except:
        bot.send_message(
            message.chat.id, "Invalid photo. To try again - send /sendphoto")


if __name__ == "__main__":
    bot.polling()
