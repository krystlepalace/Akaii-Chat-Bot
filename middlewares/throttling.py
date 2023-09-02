from typing import Any, Awaitable, Callable, Dict
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import ChatPermissions, Message, TelegramObject
import main
from datetime import datetime, timedelta


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
                if int(check_user.decode()) < 7:
                    await self.storage.redis.set(
                        name=user, value=int(check_user.decode()) + 1, ex=4
                    )
                elif int(check_user.decode()) > 7:
                    return
                else:
                    permissions = ChatPermissions()
                    permissions.can_send_messages = False
                    permissions.can_send_media_messages = False
                    permissions.can_send_stickers = False
                    permissions.can_send_animations = False
                    permissions.can_send_games = False

                    until = datetime.now() + timedelta(hours=1) 
                    alert0 = (
                            "Пользователь " + event.from_user.full_name + " заглушен"
                             )
                    alert1 = f" до {str(until)}" 

                    await event.chat.restrict(
                        user_id=event.from_user.id,
                        permissions=permissions,
                        until_date=until,
                                                )

                    await event.reply(alert0 + alert1)
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
