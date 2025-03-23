import asyncio

from botfactory import bot, dp
from handlers.start_handler import start_router


async def main():
    dp.include_routers(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except TypeError as e:
        print(e)