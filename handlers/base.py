from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
            "Привет! Это чат-менеджер, который позволяет включить или отключить автоудаление анимированных стикеров в чате."
            )

@router.message()
async def check_sticker(message: Message):
    if message.sticker:
        if message.sticker.is_video or message.sticker.is_animated:
            await message.delete()

