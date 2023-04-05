from aiogram import Bot, Dispatcher, executor
from config import TOKEN, ADMIN
from handlers import register_handlers

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

register_handlers(dp)

async def on_startup(_):
    await bot.send_message(ADMIN, "Bot is ready")
    print("Bot is working")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
