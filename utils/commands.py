from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
            BotCommand(
                command="help",
                description="Помощь по боту"
                ),
            BotCommand(
                command="animations",
                description="Включить или отключить анимированные стикеры"
                ),
            BotCommand(
                command="voice",
                description="Включить или отключить перевод ГС"
                )
            ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())

