from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from handlers.callbacks.callback_settings import SettingsCallback
from handlers.callbacks.callback_toggles import ToggleCallback


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


def settings_inline(
    anim=True, voice=True, nsfw=True, antiflood=False
) -> InlineKeyboardMarkup:
    inline_kb_full = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Анимированные стикеры: " + ("✅" if anim else "❌"),
                    callback_data=SettingsCallback(
                        parameter="anim", desc="анимированные стикеры"
                    ).pack(),
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Перевод ГС в текст: " + ("✅" if voice else "❌"),
                    callback_data=SettingsCallback(
                        parameter="voice", desc="перевод ГС в текст"
                    ).pack(),
                ),
            ],
            [
                InlineKeyboardButton(
                    text="NSFW: " + ("✅" if nsfw else "❌"),
                    callback_data=SettingsCallback(
                        parameter="nsfw", desc="NSFW"
                    ).pack(),
                )
            ],
            [
                InlineKeyboardButton(
                    text="Anti-Flood: " + ("✅" if antiflood else "❌"),
                    callback_data=SettingsCallback(
                        parameter="antiflood", desc="Anti-Flood"
                    ).pack(),
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Закрыть",
                    callback_data=SettingsCallback(
                        parameter="close", desc="Настройки закрыты"
                    ).pack(),
                )
            ],
        ]
    )

    return inline_kb_full


def close() -> InlineKeyboardMarkup:
    inline_kb_full = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Закрыть", callback_data="settings_close")]
        ]
    )

    return inline_kb_full
