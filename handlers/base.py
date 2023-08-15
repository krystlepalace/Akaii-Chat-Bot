from aiogram import Router
from aiogram.filters import Command
from aiogram.filters.text import Text

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
            "Привет! Это чат-менеджер, который позволяет включить или отключить автоудаление анимированных стикеров в чате."
            )

