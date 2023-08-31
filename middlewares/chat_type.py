from typing import Any, Awaitable, Callable, Dict
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message, TelegramObject
import main


class ChatTypeMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any]
                       ) -> Any:
        chat = None
        if event.chat.type in ['group', 'supergroup']:
            chat = await main.db.get_chat(event.chat.id)
        data["chat"] = chat
        
        return await handler(event, data)

