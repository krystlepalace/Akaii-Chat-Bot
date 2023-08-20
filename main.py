import asyncio
from aiogram import Bot, Dispatcher
from handlers import base, callback_query, administrative, content_filters
from utils.commands import set_commands
from models import database
from config import CONFIG


db = database.Database(redis_url=CONFIG.redis_url)

animations_allowed = False

bot = Bot(token=CONFIG.bot_token.get_secret_value())


# Bot startup function
async def main():
    dp = Dispatcher()
    dp.include_routers(
            base.router, 
            callback_query.router,
            administrative.router,
            content_filters.router,
            )
    
    # set commands
    await set_commands(bot)
    # start the Bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    db.r.bgsave()

