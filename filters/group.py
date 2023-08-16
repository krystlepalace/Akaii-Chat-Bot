from aiogram.types import Message
from aiogram.enums.chat_member_status import ChatMemberStatus


async def isAdmin(message: Message):
    member = await message.chat.get_member(user_id=message.from_user.id)
    return member.status == ChatMemberStatus.ADMINISTRATOR or member.status == ChatMemberStatus.CREATOR

