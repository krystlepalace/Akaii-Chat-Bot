from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.toggles import toggle_animations 
import bot

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
            "Привет! Это чат-менеджер, который позволяет включить или отключить автоудаление анимированных стикеров в чате."
            )


@router.message(Command("allow_animations"))
async def toggle_animated_stickers(message: Message):
    await message.answer(
            "Разрешить анимированные стикеры?",
            reply_markup=toggle_animations()
            )


@router.message()
async def check_sticker(message: Message):
    if not bot.animations_allowed:
        if message.sticker and (message.sticker.is_video or message.sticker.is_animated):
            await message.delete()

