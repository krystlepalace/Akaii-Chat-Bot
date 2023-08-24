from aiogram import Router
from aiogram.types import CallbackQuery
from keyboards.toggles import voice_inline, anim_inline
from aiogram import F

router = Router()


@router.callback_query(F.data.startswith("settings_"))
async def proccess_settings_menu(callback: CallbackQuery):
    if callback.data == "settings_anim":
        await callback.message.edit_text("Разрешить анимированные стикеры?")
        await callback.message.edit_reply_markup("s", anim_inline())
        await callback.answer()
    if callback.data == "settings_voice":
        await callback.message.edit_text("Разрешить перевод ГС в текст?")
        await callback.message.edit_reply_markup("s", voice_inline())
        await callback.answer()

