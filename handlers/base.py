from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F


router = Router()

alert0 = "\nВнимание! Чат бот не является администратором данного чата. Чтобы использовать полный функционал бота повысьте его привелегии"


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
    await message.answer("Добро пожаловать, " + message.new_chat_members[0].full_name)


@router.message(F.left_chat_member)
async def left(message: Message):
    await message.delete()
