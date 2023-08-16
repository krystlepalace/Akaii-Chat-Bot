from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ChatPermissions

router = Router()

@router.message(Command("ban"))
async def ban(message: Message):
    await message.chat.ban(user_id=message.reply_to_message.from_user.id, until_date=0)
    await message.answer(
            "Пользователь " + message.reply_to_message.from_user.full_name + " был заблокирован"
            )


@router.message(Command("mute"))
async def mute(message: Message):
    permissions = ChatPermissions()
    permissions.can_send_messages = False
    permissions.can_send_media_messages = False
    permissions.can_send_stickers = False
    permissions.can_send_animations = False
    permissions.can_send_games = False

    duration = int(message.text.split()[1])

    await message.chat.restrict(
            user_id=message.reply_to_message.from_user.id, 
            permissions=permissions,
            until_date=duration
            )


@router.message(Command("unban"))
async def unban(message: Message):
    await message.chat.unban(user_id=message.reply_to_message.from_user.id)
    await message.answer(
            "Пользователь " + message.reply_to_message.from_user.full_name + " был разблокирован"
            )

