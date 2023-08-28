from os import walk
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.enums.chat_member_status import ChatMemberStatus
from aiogram.filters.callback_data import CallbackData
from aiogram import F
from filters import group
import keyboards
import main

router = Router()


class ToggleCallback(CallbackData, prefix="tgl"):
    toggle: str
    status: bool
    desc: str


@router.callback_query(
    ToggleCallback.filter(F.toggle.startswith("anim")), group.IsAdminCallback()
)
async def process_toggle_anim(callback: CallbackQuery, callback_data: ToggleCallback):
    bot_member = await callback.message.chat.get_member(
        user_id=callback.message.from_user.id
    )

    if bot_member.status == ChatMemberStatus.ADMINISTRATOR:
        await main.db.set_anim(callback.message.chat.id, callback_data.status)
        await callback.message.edit_text(
            "Анимированные стикеры " + callback_data.desc, reply_markup=keyboards.toggles.close()
        )
        await callback.answer()
    else:
        await callback.message.edit_text("Бот не является администратором.")


@router.callback_query(
    ToggleCallback.filter(F.toggle.startswith("voice")), group.IsAdminCallback()
)
async def process_toggle_voice(callback: CallbackQuery, callback_data: ToggleCallback):
    bot_member = await callback.message.chat.get_member(
        user_id=callback.message.from_user.id
    )

    if bot_member.status == ChatMemberStatus.ADMINISTRATOR:
        await main.db.set_voice(callback.message.chat.id, callback_data.status)
        await callback.message.edit_text(
            "Перевод ГС в текст " + callback_data.desc, reply_markup=keyboards.toggles.close()
        )
        await callback.answer()
    else:
        await callback.message.edit_text("Бот не является администратором.")
