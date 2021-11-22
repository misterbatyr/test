import re
from telegram import(
Update,
InlineKeyboardButton,
InlineKeyboardMarkup,
update,

)
from telegram.callbackquery import CallbackQuery



from telegram.ext import (
CallbackContext, 
Updater, 
CommandHandler,  
PicklePersistence, 
Filters, 
MessageHandler,
CallbackQueryHandler,

)

from telegram.ext.messagehandler import MessageHandler
from telegram.files.sticker import MaskPosition
from telegram.message import Message
from menu import main_menu_keyboard, course_menu_keyboard
from credentials import TOKEN
from key_buttons import tele_buttons, course_menu
from message import begimai, adil, meder,Contacts, info_about_english

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Добро пожаловать Школу английского языка {username}, выберите опцию: ".format(
            username=update.effective_user.first_name \
                if update.effective_user.first_name is not None \
                else update.effective_user.username

        ),
        reply_markup=main_menu_keyboard()
    )
COURSE_REGEX = r"(?=(" + (tele_buttons[1]) + r"))"
PYTHON_REGEX = r"(?=(" + (course_menu[0]) + r"))"
TEACHERS_REGEX = r"(?=(" + (course_menu[1]) + r"))"
INFO_REGEX = r"(?=(" + (tele_buttons[2]) + r"))"
CONTACTS_REGEX = r"("+ (course_menu[1]) + r"))"

def receive_course_menu(update: Update, context: CallbackContext):
    info = re.match(COURSE_REGEX, update.message.text)
    update.message.reply_text(
        "Выберите Опцию",
        reply_markup=course_menu_keyboard()
    )

def receive_course_info_price(update: Update, context: CallbackContext):
    info = re.match(PYTHON_REGEX, update.message.text)
    update.message.reply_text(
        "Price is sdfsfd\nShedule is 18:00",
    )


def receive_course_contacts(update: Update, context: CallbackContext):
    info = re.match(CONTACTS_REGEX, update.message.text)
    update.message.reply_text(
        Contacts
        
    )

def python_inline_menu(update: Update, context: CallbackContext):
    info = re.match(TEACHERS_REGEX, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Begimai", callback_data='begimai')],
        [InlineKeyboardButton("Meder", callback_data='meder')],
        [InlineKeyboardButton("Adil", callback_data='adil')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(

        'Выберите преподавателя',
        reply_markup=reply_markup
    )

def info_inline_menu(update: Update, context: CallbackContext):
    info = re.match(INFO_REGEX, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Фото", callback_data='anglish_photo')],
        [InlineKeyboardButton("Информация о нас", callback_data='anglish_info')],
        [InlineKeyboardButton("Локация", callback_data='anglish_location')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(

        'Что вас интересует?',
        reply_markup=reply_markup
    )

def inline_buttons(update: Update, context: CallbackContext):
    # info = re.match(COURSE_REGEX, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Фото", callback_data='anglish_photo')],
        [InlineKeyboardButton("Информация о нас", callback_data='anglish_info')],
        [InlineKeyboardButton("Локация", callback_data='anglish_location')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    

    query= update.callback_query
    query.answer()
    
    if query.data == 'anglish_photo':
        query.message.reply_photo(
           open('700-nw.jpg', 'rb')
        )
    if query.data == 'anglish_info':
        query.message.reply_text(
            info_about_english
        ) 
    if query.data == 'anglish_location':
        query.message.reply_location(
            longitude=74.6342282200863,
            latitude=42.87566006583323
        ) 
    if query.data == 'begimai':
        query.message.reply_text(
           text="Менеджер тел: 0999379992"
        )
    if query.data == 'meder':
        query.message.reply_text(
            text="Преподаватель тел: 0777737777"
        ) 
    if query.data == 'adil':
        query.message.reply_text(
            text="Преподаватель тел: 0777770770"
        ) 

updater = Updater(TOKEN,persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE_REGEX),
    receive_course_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE_REGEX),
        receive_course_contacts
    
))
# def inline_buttons(update: Update, context: CallbackContext):
#     query.edit_message_text(
#             text=begimai,
#     reply_markup = InlineKeyboardMarkup(Contacts)


updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PYTHON_REGEX),
    receive_course_info_price
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(TEACHERS_REGEX),
    python_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(INFO_REGEX),
    info_inline_menu
))

updater.dispatcher.add_handler(CallbackQueryHandler(inline_buttons))

updater.start_polling()
updater.idle()
