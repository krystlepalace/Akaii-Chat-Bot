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
                description="Включить или выключить анимированные стикеры"
                )
            ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())

