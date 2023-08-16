from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def anim_inline() -> InlineKeyboardMarkup:
    inline_kb_full = InlineKeyboardMarkup(inline_keyboard=[
        [
         InlineKeyboardButton(text="Разрешить", callback_data="anim0"),
         InlineKeyboardButton(text="Запретить", callback_data="anim1")
            ]
        ])


    return inline_kb_full

