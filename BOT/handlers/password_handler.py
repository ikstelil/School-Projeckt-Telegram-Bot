from aiogram import types
from password_generator import PasswordGenerator
from keyboards import user_keyboard

password_generator = PasswordGenerator()

async def generate_password_handler(callback_query: types.CallbackQuery):
    password = password_generator.generate_password()
    await callback_query.message.answer(f"{password}",reply_markup=user_keyboard)
    await callback_query.message.delete()

async def set_password_length_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Пожалуйста, пришлите мне сообщение с желаемой длиной пароля (до 100 символов):")
    await callback_query.message.delete()

async def process_password_length_message(message: types.Message):
    try:
        length = int(message.text)
        if length > 100:
            await message.answer("Введите пароль длиной не более 100 символов.")
            await message.delete()
            return
        password_generator.length = length
        password = password_generator.generate_password()
        await message.answer(f"{password}",reply_markup=user_keyboard)
        await message.delete()
    except ValueError:
        await message.answer("Пожалуйста, введите корректное число")
        await message.delete()
