from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F
import main
from models.model import Chat


router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Привет!"
        + "\nЭто чат-менеджер, который может "
        + "Отключать анимированные стикеры в чате."
        + "\nЧтобы узнать больше отправь /help"
    )


@router.message(Command("help"))
async def help(message: Message):
    await message.answer(
        "Помощь по боту.\n\nЭто бот чат-менеджер, который умеет:"
        + "\n   - Фильтровать анимированные стикеры"
        + "\n   - Фильтровать сообщения по запрещенным словам"
        + "\n   - Приветствовать вступающих в чат"
        + "\n   - Переводить ГС в текст"
        + "\n   - А также имеет базовые комманды для модерирования(мут, бан, кик)"
        + "\n\nКомманды:"
        + "\n/help - Помощь"
        + "\n/animations - Включить/Выключить анимированные стикеры"
        + "\n/ban - Забанить участника чата"
        + "\n/unban - Разблокировать участника чата"
        + "\n/mute - Заглушить участника чата"
        + "\n/unmute - Разглушить участника чата"
        + "\n\n Приятного пользования!"
    )


@router.message(F.new_chat_members)
async def greeting(message: Message):
    bot = await main.bot.me()
    for member in message.new_chat_members:
        if member.id == bot.id:
            await main.db.reg_chat(
                    chat=Chat(
                        chat_id=message.chat.id,
                        anim=True,
                        voice=True
                        )
                    )
        await message.answer("Добро пожаловать, " + member.full_name)


@router.message(F.left_chat_member)
async def left(message: Message):
    await message.answer("Прощай, " + message.left_chat_member.full_name)
    await message.delete()

