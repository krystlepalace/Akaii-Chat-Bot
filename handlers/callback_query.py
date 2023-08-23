from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.enums.chat_member_status import ChatMemberStatus
from models import db_chat
from filters import group

router = Router()


@router.callback_query()
async def process_toggle_callback(callback: CallbackQuery):
    if await group.isAdmin(callback.message, callback.from_user.id):
        bot_member = await callback.message.chat.get_member(
            user_id=callback.message.from_user.id
        )
        if bot_member.status == ChatMemberStatus.ADMINISTRATOR:
            chat = db_chat.Chat(callback.message.chat.id)

            if callback.data == "anim0":
                chat.set_anim(True)
                await callback.message.answer("Аминированные стикеры разрешены!")
                await callback.answer()
            if callback.data == "anim1":
                chat.set_anim(False)
                await callback.message.answer("Анимированные стикеры запрещены.")
                await callback.answer()
            if callback.data == "voice0":
                chat.set_voice(True)
                await callback.message.answer("Перевод голосвых сообщений включен.")
                await callback.answer()
            if callback.data == "voice1":
                chat.set_voice(False)
                await callback.message.answer("Перевод голосовых сообщений отключен.")
                await callback.answer()

        else:
            await callback.message.answer("Бот не является администратором.")
    else:
        await callback.message.answer("Вы не являетесь администратором.")
        await callback.answer()
