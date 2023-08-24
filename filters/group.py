from aiogram.types import Message, CallbackQuery
from aiogram.enums.chat_member_status import ChatMemberStatus
from aiogram.filters import BaseFilter


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message):
        chat_member = await message.chat.get_member(user_id=message.from_user.id)
        return (
                chat_member.status == ChatMemberStatus.ADMINISTRATOR
                or chat_member.status == ChatMemberStatus.CREATOR
                )


class IsAdminCallback(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        chat_member = await callback.message.chat.get_member(
                user_id=callback.from_user.id
                )
        return (
                chat_member.status == ChatMemberStatus.ADMINISTRATOR
                or chat_member.status == ChatMemberStatus.CREATOR
                )

