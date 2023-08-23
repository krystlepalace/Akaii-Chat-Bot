from aiogram import Router
from aiogram import exceptions
from aiogram.filters import Command
from aiogram.types import Message, ChatPermissions
from datetime import datetime, timedelta
from filters import group

router = Router()


@router.message(Command("ban"))
async def ban(message: Message):
    if await group.isAdmin(message):
        try:
            await message.chat.ban(
                user_id=message.reply_to_message.from_user.id, until_date=0
            )
            await message.answer(
                "Пользователь "
                + message.reply_to_message.from_user.full_name
                + " был заблокирован"
            )
        except exceptions.TelegramBadRequest:
            await message.answer("Бот не является администратором!")
    else:
        await message.answer("Вы не являетесь администратором.")


@router.message(Command("mute"))
async def mute(message: Message):
    if await group.isAdmin(message):
        permissions = ChatPermissions()
        permissions.can_send_messages = False
        permissions.can_send_media_messages = False
        permissions.can_send_stickers = False
        permissions.can_send_animations = False
        permissions.can_send_games = False

        try:
            duration = int(message.text.split()[1])
        except IndexError:
            duration = 0

        until = datetime.now() + timedelta(hours=duration) if duration > 0 else 1
        alert0 = (
            "Пользователь " + message.reply_to_message.from_user.full_name + " заглушен"
        )
        alert1 = f" до {str(until)}" if duration > 0 else " навсегда"

        try:
            await message.chat.restrict(
                user_id=message.reply_to_message.from_user.id,
                permissions=permissions,
                until_date=until,
            )

            await message.answer(alert0 + alert1)
        except exceptions.TelegramBadRequest:
            await message.answer("Бот не является администратором!")
    else:
        await message.answer("Вы не являетесь администратором.")


@router.message(Command("unmute"))
async def unmute(message: Message):
    if await group.isAdmin(message):
        permissions = ChatPermissions()
        permissions.can_send_messages = True
        permissions.can_send_media_messages = True
        permissions.can_send_stickers = True
        permissions.can_send_animations = True
        permissions.can_send_games = True

        try:
            await message.chat.restrict(
                user_id=message.reply_to_message.from_user.id,
                permissions=permissions,
                until_date=1,
            )

            await message.answer(
                "Пользователь "
                + message.reply_to_message.from_user.full_name
                + " вновь получил право голоса!"
            )
        except exceptions.TelegramBadRequest:
            await message.answer("Бот не является администратором!")
    else:
        await message.answer("Вы не являетесь администратором.")


@router.message(Command("unban"))
async def unban(message: Message):
    if await group.isAdmin(message):
        try:
            await message.chat.unban(user_id=message.reply_to_message.from_user.id)
            await message.answer(
                "Пользователь "
                + message.reply_to_message.from_user.full_name
                + " был разблокирован"
            )
        except exceptions.TelegramBadRequest:
            await message.answer("Бот не является администратором!")
    else:
        await message.answer("Вы не являетесь администратором.")
