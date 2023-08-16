from aiogram import Router
from aiogram.types import CallbackQuery
import bot

router = Router()

@router.callback_query()
async def process_anim_toggle_callback(callback: CallbackQuery):
    if callback.data == 'anim0':
        bot.animations_allowed = True
        await callback.message.answer("Аминированные стикеры разрешены!")
        await callback.answer()
    if callback.data == 'anim1':
        bot.animations_allowed = False
        await callback.message.answer("Анимированные стикеры запрещены.")
        await callback.answer()

