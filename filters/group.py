from aiogram.types import Message
from aiogram.enums.chat_member_status import ChatMemberStatus
from aiogram.filters import BaseFilter


async def isAdmin(message: Message, user_id=None):
    if user_id is None:
        user_id = message.from_user.id

    member = await message.chat.get_member(user_id=user_id)
    return (
        member.status == ChatMemberStatus.ADMINISTRATOR
        or member.status == ChatMemberStatus.CREATOR
    )


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message):
        chat_member = await message.chat.get_member(user_id=message.from_user.id)
        return (
                chat_member.status == ChatMemberStatus.ADMINISTRATOR
                or chat_member.status == ChatMemberStatus.CREATOR
                )

