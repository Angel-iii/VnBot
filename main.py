import asyncio
from aiogram import Bot, Dispatcher
bot = Bot(token='7720308388:AAFllQjBGydz0OI9T_hnwee-nPI3nO-3rhA')
from app.handlers import router



async def main():
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
