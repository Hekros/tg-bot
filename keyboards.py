from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def start_kb():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Заполнить анкету")]],
        resize_keyboard=True
    )
