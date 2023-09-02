from aiogram import Router
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery
from keyboards.toggles import anim_inline, voice_inline, nsfw_inline, antiflood_inline
from aiogram import F
from filters import group


router = Router()


class SettingsCallback(CallbackData, prefix="settings"):
    parameter: str
    desc: str


settings_keyboards = {
    "anim": anim_inline(),
    "voice": voice_inline(),
    "nsfw": nsfw_inline(),
    "antiflood": antiflood_inline(),
    "close": None,
}


@router.callback_query(
    SettingsCallback.filter(F.parameter.startswith(("anim", "nsfw"))),
    group.IsAdminCallback(),
)
async def process_parameters0_callback(
    callback: CallbackQuery, callback_data: CallbackData
):
    await callback.message.edit_text(
        text=f"Разрешить {callback_data.desc}?",
        reply_markup=settings_keyboards[callback_data.parameter],
    )
    await callback.answer()


@router.callback_query(
    SettingsCallback.filter(F.parameter.startswith(("voice", "antiflood"))),
    group.IsAdminCallback(),
)
async def process_parameters1_callback(
    callback: CallbackQuery, callback_data: CallbackData
):
    await callback.message.edit_text(
        text=f"Включить {callback_data.desc}?",
        reply_markup=settings_keyboards[callback_data.parameter],
    )
    await callback.answer()


@router.callback_query(
    SettingsCallback.filter(F.parameter.startswith("close")),
    group.IsAdminCallback(),
)
async def process_close_callback(callback: CallbackQuery, callback_data: CallbackData):
    await callback.message.edit_text(
        text=f"{callback_data.desc}",
        reply_markup=settings_keyboards[callback_data.parameter],
    )
    await callback.answer()
