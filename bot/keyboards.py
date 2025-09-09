from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_action_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔐 Зашифровать"), KeyboardButton(text="🔓 Расшифровать")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

def get_restart_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔁 Начать заново")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
