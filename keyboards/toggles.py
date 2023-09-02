from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from handlers.callbacks import callback_toggles, callback_settings


ToggleCallback = callback_toggles.ToggleCallback
SettingsCallback = callback_settings.SettingsCallback

def anim_inline() -> InlineKeyboardMarkup:
    inline_kb_full = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Разрешить",
                    callback_data=ToggleCallback(
                        toggle="anim0",
                        status=True,
                        desc="разрешены!",
                    ).pack(),
                ),
                InlineKeyboardButton(
                    text="Запретить",
                    callback_data=ToggleCallback(
                        toggle="anim1",
                        status=False,
                        desc="запрещены.",
                    ).pack(),
                ),
            ]
        ]
    )

    return inline_kb_full


def voice_inline() -> InlineKeyboardMarkup:
    inline_kb_full = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Включить",
                    callback_data=ToggleCallback(
                        toggle="voice0",
                        status=True,
                        desc="включен.",
                    ).pack(),
                ),
                InlineKeyboardButton(
                    text="Отключить",
                    callback_data=ToggleCallback(
                        toggle="voice1",
                        status=False,
                        desc="отключен.",
                    ).pack(),
                ),
            ]
        ]
    )

    return inline_kb_full


def nsfw_inline() -> InlineKeyboardMarkup:
    inline_kb_full = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Разрешить",
                    callback_data=ToggleCallback(
                        toggle="nsfw0",
                        status=True,
                        desc="разрешено.",
                    ).pack(),
                ),
                InlineKeyboardButton(
                    text="Запретить",
                    callback_data=ToggleCallback(
                        toggle="nsfw1",
                        status=False,
                        desc="запрещено.",
                    ).pack(),
                ),
            ]
        ]
    )

    return inline_kb_full


def antiflood_inline() -> InlineKeyboardMarkup:
    inline_kb_full = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Включить",
                    callback_data=ToggleCallback(
                        toggle="antiflood0", status=True, desc="включен."
                    ).pack(),
                ),
                InlineKeyboardButton(
                    text="Выключить",
                    callback_data=ToggleCallback(
                        toggle="antiflood1", status=False, desc="выключен."
                    ).pack(),
                ),
            ]
        ]
    )

    return inline_kb_full
