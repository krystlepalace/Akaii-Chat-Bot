from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeAllChatAdministrators


async def set_commands(bot: Bot):
    default_commands = [
            BotCommand(
                command="help",
                description="Помощь по боту"
                ),
                ]

    admin_commands = [
            BotCommand(
                command="animations",
                description="Включить или отключить анимированные стикеры"
                ),
            BotCommand(
                command="voice",
                description="Включить или отключить перевод ГС"
                ),
            BotCommand(
                command="ban",
                description="Заблокировать пользователя"
                ),
            BotCommand(
                command="unban",
                description="Разблокировать пользователя"
                ),
            BotCommand(
                command="mute",
                description="Заглушить пользователя"
                ),
            BotCommand(
                command="unmute",
                description="Вернуть право голоса"
                )
                ]

    await bot.set_my_commands(default_commands, BotCommandScopeDefault())
    await bot.set_my_commands(admin_commands, BotCommandScopeAllChatAdministrators())

