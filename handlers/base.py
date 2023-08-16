from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.toggles import anim_inline
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


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
            "Привет! Это чат-менеджер, который позволяет включить или отключить автоудаление анимированных стикеров в чате."
            )


@router.message(Command("animations"))
async def toggle_animated_stickers(message: Message):
    await message.answer(
            "Разрешить анимированные стикеры?",
            reply_markup=anim_inline()
            )


@router.message()
async def check_sticker(message: Message):
    if not bot.animations_allowed:
        if message.sticker and (message.sticker.is_video or message.sticker.is_animated):
            await message.delete()

