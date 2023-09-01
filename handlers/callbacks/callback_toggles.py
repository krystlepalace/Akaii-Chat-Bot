from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.enums.chat_member_status import ChatMemberStatus
from aiogram.filters.callback_data import CallbackData
from aiogram import F
from middlewares import bot_priveleges
from filters import group
import keyboards
import main

router = Router()
router.callback_query.middleware(bot_priveleges.BotIsAdminCallbackMiddleware())


class ToggleCallback(CallbackData, prefix="tgl"):
    toggle: str
    status: bool
    desc: str


@router.callback_query(
    ToggleCallback.filter(F.toggle.startswith("anim")), group.IsAdminCallback()
)
async def process_toggle_anim(callback: CallbackQuery, callback_data: ToggleCallback):
    await main.db.set_anim(callback.message.chat.id, callback_data.status)
    await callback.message.edit_text(
            "Анимированные стикеры " + callback_data.desc, reply_markup=keyboards.toggles.close()
        )
    await callback.answer()


@router.callback_query(
    ToggleCallback.filter(F.toggle.startswith("voice")), group.IsAdminCallback()
)
async def process_toggle_voice(callback: CallbackQuery, callback_data: ToggleCallback): 
    await main.db.set_voice(callback.message.chat.id, callback_data.status)
    await callback.message.edit_text(
            "Перевод ГС в текст " + callback_data.desc, reply_markup=keyboards.toggles.close()
        )
    await callback.answer()


@router.callback_query(
    ToggleCallback.filter(F.toggle.startswith("nsfw")), group.IsAdminCallback()
)
async def process_toggle_nsfw(callback: CallbackQuery, callback_data: ToggleCallback): 
    await main.db.set_nsfw(callback.message.chat.id, callback_data.status)
    await callback.message.edit_text(
            "NSFW " + callback_data.desc, reply_markup=keyboards.toggles.close()
        )
    await callback.answer()


@router.callback_query(
        ToggleCallback.filter(F.toggle.startswith("antiflood")), group.IsAdminCallback()
        )
async def processs_toggle_antiflood(callback: CallbackQuery, callback_data: ToggleCallback):
    await main.db.set_antiflood(callback.message.chat.id, callback_data.status)
    await callback.message.edit_text(
            "Anti-Flood " + callback_data.desc, reply_markup=keyboards.toggles.close()
            )
    await callback.answer()

