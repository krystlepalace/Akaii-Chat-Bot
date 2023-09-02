from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from handlers.callbacks.callback_settings import SettingsCallback


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
