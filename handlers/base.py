from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.toggles import anim_inline
import bot

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
            "Привет!" \
            + "\nЭто чат-менеджер, который может " \
            + "Отключать анимированные стикеры в чате." \
            + "\nЧтобы узнать больше отправь /help" 
            )


@router.message(Command("help"))
async def help(message: Message):
    await message.answer(
            "Помощь по боту.\n\nЭто бот чат-менеджер, который умеет:" \
                    + "\n   - Фильтровать анимированные стикеры" \
                    + "\n   - Фильтровать сообщения по запрещенным словам" \
                    + "\n   - Приветствовать вступающих в чат" \
                    + "\n   - Переводить ГС в текст" \
                    + "\n   - А также имеет базовые комманды для модерирования(мут, бан, кик)" \
                    + "\n\nКомманды:" \
                    + "\n/help - Помощь" \
                    + "\n/animations - Включить/Выключить анимированные стикеры" \
                    + "\n/ban - Забанить участника чата" \
                    + "\n/mute - Замутить участника чата" \
                    + "\n\n Приятного пользования!"
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

