from typing import Any, Awaitable, Callable, Dict
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.enums.chat_member_status import ChatMemberStatus
from aiogram.types import Message, CallbackQuery, TelegramObject
import main


class BotIsAdminMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        bot = await main.bot.me()
        bot_member = await event.chat.get_member(
        user_id=bot.id
        )
        if bot_member.status == ChatMemberStatus.ADMINISTRATOR:
            return await handler(event, data)
        else:
            await event.answer("Бот не является администратором.")
            return


class BotIsAdminCallbackMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        bot = await main.bot.me()
        bot_member = await event.message.chat.get_member(
        user_id=bot.id
        )
        if bot_member.status == ChatMemberStatus.ADMINISTRATOR:
            return await handler(event, data)
        else:
            await event.message.edit_text("Бот не является администратором.")
            return

