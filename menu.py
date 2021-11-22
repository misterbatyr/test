import telegram
from key_buttons import tele_buttons, course_menu


def main_menu_keyboard():
    keyboard=([
        [
            telegram.KeyboardButton(tele_buttons[0]),
            telegram.KeyboardButton(tele_buttons[1]),
            telegram.KeyboardButton(tele_buttons[2]),
        ]   
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_timekeyboard=False
    )

def course_menu_keyboard():
    keyboard=([
        [
            telegram.KeyboardButton(course_menu[0]),
            telegram.KeyboardButton(course_menu[1])
        ]   
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_timekeyboard=False
    )







