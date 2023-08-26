import asyncio
from aiogram import Bot, Dispatcher
from handlers import base, administrative, content_filters
from handlers.callbacks import callback_settings, callback_toggles
from utils.commands import set_commands
from models import database
from config import CONFIG


db = database.Database(mongodb_url=CONFIG.mongodb.get_secret_value())
bot = Bot(token=CONFIG.bot_token.get_secret_value())


# Bot startup function
async def main():
    dp = Dispatcher()
    dp.include_routers(
        base.router,
        callback_settings.router,
        callback_toggles.router,
        administrative.router,
        content_filters.router,
    )

    # set commands
    await set_commands(bot)
    # start the Bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

