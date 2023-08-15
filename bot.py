from decouple import config
import asyncio
from aiogram import Bot, Dispatcher
from handlers import base


TOKEN = config("BOT_TOKEN")

# Bot startup function
async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(base.router)

    # start the bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

