from aiogram import Router
from aiogram.types import CallbackQuery
from keyboards.toggles import voice_inline, anim_inline
from aiogram import F
from asyncio import sleep
from filters import group

router = Router()


@router.callback_query(F.data.startswith("settings_"), group.IsAdminCallback())
async def proccess_settings_menu(callback: CallbackQuery):
    if callback.data == "settings_anim":
        await callback.message.edit_text("Разрешить анимированные стикеры?",
                                         reply_markup=anim_inline())
        await sleep(10)
        await callback.answer()
        await callback.message.delete()
    if callback.data == "settings_voice":
        await callback.message.edit_text("Разрешить перевод ГС в текст?", 
                                         reply_markup=voice_inline())
        await sleep(10)
        await callback.answer()
        await callback.message.delete()
    if callback.data == "settings_close":
        await callback.message.edit_text("Настройки закрыты.")
        await callback.answer()

