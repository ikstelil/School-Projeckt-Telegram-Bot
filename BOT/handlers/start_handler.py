from aiogram import types
from keyboards import user_keyboard

async def start_handler(message: types.Message):
    await message.reply("Привет!",reply_markup=user_keyboard)
