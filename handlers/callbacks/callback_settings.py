from aiogram import Router
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery
from keyboards import toggles
from aiogram import F
from filters import group


router = Router()


settings_keyboards = {
    "anim": toggles.anim_inline(),
    "voice": toggles.voice_inline(),
    "nsfw": toggles.nsfw_inline(),
    "antiflood": toggles.antiflood_inline(),
    "close": None,
}


class SettingsCallback(CallbackData, prefix="settings"):
    parameter: str
    desc: str


@router.callback_query(
    SettingsCallback.filter(F.data.startswith(("anim", "nsfw"))),
    group.IsAdminCallback(),
)
async def process_anim_callback(callback: CallbackQuery, callback_data: CallbackData):
    await callback.message.edit_text(
        text=f"Разрешить {callback_data.desc}?",
        reply_markup=settings_keyboards[callback_data.parameter],
    )


@router.callback_query(
    SettingsCallback.filter(F.data.startswith(("voice", "antiflood"))),
    group.IsAdminCallback(),
)
async def process_anim_callback(callback: CallbackQuery, callback_data: CallbackData):
    await callback.message.edit_text(
        text=f"Включить {callback_data.desc}?",
        reply_markup=settings_keyboards[callback_data.parameter],
    )


@router.callback_query(
    SettingsCallback.filter(F.data.startswith("close")),
    group.IsAdminCallback(),
)
async def process_anim_callback(callback: CallbackQuery, callback_data: CallbackData):
    await callback.message.edit_text(
        text=f"{callback_data.desc}",
        reply_markup=settings_keyboards[callback_data.parameter],
    )
