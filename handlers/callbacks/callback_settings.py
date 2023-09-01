from aiogram import Router
from aiogram.types import CallbackQuery
from keyboards.toggles import nsfw_inline, voice_inline, anim_inline, antiflood_inline
from aiogram import F
from filters import group


router = Router()


@router.callback_query(F.data.startswith("settings_"), group.IsAdminCallback())
async def proccess_settings_menu(callback: CallbackQuery):
    if callback.data == "settings_anim":
        await callback.message.edit_text("Разрешить анимированные стикеры?",
                                         reply_markup=anim_inline()) 
    if callback.data == "settings_voice":
        await callback.message.edit_text("Разрешить перевод ГС в текст?", 
                                         reply_markup=voice_inline())
    if callback.data == "settings_nsfw":
        await callback.message.edit_text("Разрешить NSFW?",
                                         reply_markup=nsfw_inline())
    if callback.data == "settings_antiflood":
        await callback.message.edit_text("Включить Anti-Flood?",
                                         reply_markup=antiflood_inline())
    if callback.data == "settings_close":
        await callback.message.edit_text("Настройки закрыты.",
                                         reply_markup=None)
    await callback.answer()

