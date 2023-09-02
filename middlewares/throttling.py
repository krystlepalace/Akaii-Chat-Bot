from typing import Any, Awaitable, Callable, Dict
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import ChatPermissions, Message, TelegramObject
import main
from datetime import datetime, timedelta

from utils.neuro.nudenet.nude_checker import check


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
            user = f"user{event.from_user.id}_flood"
            check_user = await self.storage.redis.get(name=user)
            if check_user:
                check_user = int(check_user.decode())
                if check_user < 7:
                    await self.storage.redis.set(
                        name=user, value=check_user + 1, ex=4
                    )
                elif check_user > 7:
                    return
                else:
                    permissions = ChatPermissions()
                    permissions.can_send_messages = False
                    
                    until = datetime.now() + timedelta(hours=1)  

                    await event.chat.restrict(
                        user_id=event.from_user.id,
                        permissions=permissions,
                        until_date=until,
                                                )

                    await event.reply("Пользователь" + event.from_user.full_name + "был заглушен за флуд.")
            else:
                await self.storage.redis.set(name=user, value=1, ex=4)
        return await handler(event, data)


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, storage: RedisStorage):
        self.storage = storage

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        if not data.get("command"):
            return await handler(event, data)
        user = f"user{event.from_user.id}_command"
        check_user = await self.storage.redis.get(name=user)
        if check_user:
            if int(check_user.decode()) == 1:
                await self.storage.redis.set(name=user, value=0, ex=3)
                return
            return

        await self.storage.redis.set(name=user, value=1, ex=3)
        return await handler(event, data)
