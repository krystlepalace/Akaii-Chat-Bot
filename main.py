import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from middlewares.throttling import AntiFloodMiddleware, ThrottlingMiddleware
from handlers import base, administrative, content_filters
from handlers.callbacks import callback_settings, callback_toggles
from utils.commands import set_commands
from models import database
from config import CONFIG

storage = RedisStorage.from_url(CONFIG.redis_url)
db = database.Database(mongodb_url=CONFIG.mongodb.get_secret_value())
bot = Bot(token=CONFIG.bot_token.get_secret_value())


# Bot startup function
async def main():
    dp = Dispatcher()

    # Setup routers
    dp.include_routers(
        base.router,
        callback_settings.router,
        callback_toggles.router,
        administrative.router,
        content_filters.router,
    )

    # Setup middlewares
    dp.message.middleware.register(ThrottlingMiddleware(storage=storage))
    dp.message.middleware.register(AntiFloodMiddleware(storage=storage))
    
    # set commands
    await set_commands(bot)
    # start the Bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

