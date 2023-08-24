from aiogram.types import Message, CallbackQuery
from aiogram.enums.chat_member_status import ChatMemberStatus
from aiogram.filters import BaseFilter

# Just checking if user has admin priveleges without notifying if he has'nt
#class IsAdmin(BaseFilter):
#    async def __call__(self, message: Message):
#        chat_member = await message.chat.get_member(user_id=message.from_user.id)
#        return (
#                chat_member.status == ChatMemberStatus.ADMINISTRATOR
#                or chat_member.status == ChatMemberStatus.CREATOR
#                )

# Bot will notify if user is not an admin
class IsAdmin(BaseFilter):
    async def __call__(self, message: Message):
        chat_member = await message.chat.get_member(user_id=message.from_user.id)
        if chat_member.status == ChatMemberStatus.ADMINISTRATOR \
        or chat_member.status == ChatMemberStatus.CREATOR:
            return True
        else:
            await message.reply("Вы не являетесь администратором.")
            return False


# Just checking if user has admin priveleges without notifying if he has'nt
#class IsAdminCallback(BaseFilter):
#    async def __call__(self, callback: CallbackQuery):
#        chat_member = await callback.message.chat.get_member(
#                user_id=callback.from_user.id
#                )
#        return (
#                chat_member.status == ChatMemberStatus.ADMINISTRATOR
#                or chat_member.status == ChatMemberStatus.CREATOR
#                )

# Bot will notify if user is not an admin
class IsAdminCallback(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        chat_member = await callback.message.chat.get_member(
        user_id=callback.from_user.id)

        if chat_member.status == ChatMemberStatus.ADMINISTRATOR \
        or chat_member.status == ChatMemberStatus.CREATOR:
            return True
        else:
            await callback.answer(
                text="Вы не являетесь администратором", 
                show_alert=True
                )
            return False

