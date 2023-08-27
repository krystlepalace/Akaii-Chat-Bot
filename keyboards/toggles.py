from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def anim_inline() -> InlineKeyboardMarkup:
    inline_kb_full = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Разрешить", callback_data="anim0"),
                InlineKeyboardButton(text="Запретить", callback_data="anim1"),
            ]
        ]
    )

    return inline_kb_full


def voice_inline() -> InlineKeyboardMarkup:
    inline_kb_full = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Включить", callback_data="voice0"),
                InlineKeyboardButton(text="Отключить", callback_data="voice1"),
            ]
        ]
    )

    return inline_kb_full


def settings_inline(anim=True, voice=True) -> InlineKeyboardMarkup:
    inline_kb_full = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Анимированные стикеры: " + ("✅" if anim else "❌"),
                    callback_data="settings_anim",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Перевод ГС в текст: " + ("✅" if voice else "❌"), 
                    callback_data="settings_voice"
                ),
            ],
        ]
    )

    return inline_kb_full

