from decouple import config
import asyncio
from aiogram import Bot, Dispatcher
from handlers import base, callback_query
from utils.commands import set_commands


TOKEN = config("BOT_TOKEN")
animations_allowed = False

# Bot startup function
async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(base.router, callback_query.router)
    
    # set commands
    await set_commands(bot)
    # start the bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

