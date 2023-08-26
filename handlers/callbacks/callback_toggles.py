from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.enums.chat_member_status import ChatMemberStatus
from aiogram import F
from asyncio import sleep
from filters import group
import main

router = Router()


@router.callback_query(F.data.startswith("anim"), group.IsAdminCallback())
async def process_toggle_anim(callback: CallbackQuery):
    bot_member = await callback.message.chat.get_member(
        user_id=callback.message.from_user.id
    )
    if bot_member.status == ChatMemberStatus.ADMINISTRATOR:
        if callback.data == "anim0":
            await main.db.set_anim(callback.message.chat.id, True)
            await callback.message.edit_text("Анимированные стикеры разрешены!")
            await callback.answer()
        if callback.data == "anim1":
            await main.db.set_anim(callback.message.chat.id, False)
            await callback.message.edit_text("Анимированные стикеры запрещены.")
            await callback.answer()

        await sleep(10)
        await callback.message.delete()
    else:
        await callback.message.edit_text("Бот не является администратором.")


@router.callback_query(F.data.startswith("voice"), group.IsAdminCallback())
async def process_toggle_voice(callback: CallbackQuery):
    bot_member = await callback.message.chat.get_member(
        user_id=callback.message.from_user.id
    )
    if bot_member.status == ChatMemberStatus.ADMINISTRATOR:
        if callback.data == "voice0":
            await main.db.set_voice(callback.message.chat.id, True)
            await callback.message.edit_text("Перевод голосовых сообщений включен.")
            await callback.answer()
        if callback.data == "voice1":
            await main.db.set_voice(callback.message.chat.id, False)
            await callback.message.edit_text("Перевод голосовых сообщений отключен.")
            await callback.answer()

        await sleep(10)
        await callback.message.delete()
    else:
        await callback.message.edit_text("Бот не является администратором.")
