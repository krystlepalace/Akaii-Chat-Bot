from typing import Any, Awaitable, Callable, Dict
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import Message, TelegramObject
import main
from handlers.administrative import mute


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, storage: RedisStorage):
        self.storage = storage

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        if event.sticker or event.photo:
            return await handler(event, data)

        user = f"user{event.from_user.id}"
        check_user = await self.storage.redis.get(name=user)
        if check_user:
            if int(check_user.decode()) == 1:
                await self.storage.redis.set(name=user, value=0, ex=3)
                return
            return

        await self.storage.redis.set(name=user, value=1, ex=3)
        return await handler(event, data)


class AntiFloodMiddleware(BaseMiddleware):
    def __init__(self, storage: RedisStorage):
        self.storage = storage

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        chat = await main.db.get_chat(event.chat.id)
        if (not chat is None) and chat.get("antiflood"):
            user = f"user{event.from_user.id}"
            check_user = await self.storage.redis.get(name=user)
            if check_user:
                if int(check_user.decode()) < 7:
                    await self.storage.redis.set(
                        name=user, value=check_user.decode() + 1, ex=2
                    )
                else:
                    await event.reply(text="/mute 1")
                    await event.answer(
                        "Пользователь "
                        + event.from_user.full_name
                        + " был заглушен за флуд"
                    )
            else:
                await self.storage.redis.set(name=user, value=1, ex=2)
        return await handler(event, data)
