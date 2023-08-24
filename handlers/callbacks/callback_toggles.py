from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.enums.chat_member_status import ChatMemberStatus
from aiogram import F
from models import db_chat
from filters import group

router = Router()


@router.callback_query(F.data.startswith("anim"), group.IsAdminCallback())
async def process_toggle_anim(callback: CallbackQuery):
    bot_member = await callback.message.chat.get_member(
            user_id=callback.message.from_user.id
        )
    if bot_member.status == ChatMemberStatus.ADMINISTRATOR:
        chat = db_chat.Chat(callback.message.chat.id)

        if callback.data == "anim0":
            chat.set_anim(True)
            await callback.message.edit_text("Аминированные стикеры разрешены!")
            await callback.answer()
        if callback.data == "anim1":
            chat.set_anim(False)
            await callback.message.edit_text("Анимированные стикеры запрещены.")
            await callback.answer()
    else:
        await callback.message.edit_text("Бот не является администратором.")


@router.callback_query(F.data.startswith("voice"), group.IsAdminCallback())
async def process_toggle_voice(callback: CallbackQuery):
    bot_member = await callback.message.chat.get_member(
            user_id=callback.message.from_user.id
        )
    if bot_member.status == ChatMemberStatus.ADMINISTRATOR:
        chat = db_chat.Chat(callback.message.chat.id)

        if callback.data == "voice0":
            chat.set_voice(True)
            await callback.message.edit_text("Перевод голосвых сообщений включен.")
            await callback.answer()
        if callback.data == "voice1":
            chat.set_voice(False)
            await callback.message.edit_text("Перевод голосовых сообщений отключен.")
            await callback.answer()

    else:
        await callback.message.edit_text("Бот не является администратором.")
