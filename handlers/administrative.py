from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("ban"))
async def ban(message: Message):
    pass

@router.message(Command("mute"))
async def mute(message: Message):
    pass

