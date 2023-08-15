from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def toggle_animations() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Разрешить")
    kb.button(text="Запретить")
    kb.adjust(2)

    return kb.as_markup(resize_keyboard=True)

