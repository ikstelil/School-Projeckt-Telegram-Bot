from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def create_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    button_do_generate = InlineKeyboardButton("Сгенерировать пароль", callback_data="generate_password")
    button_set_value = InlineKeyboardButton("Установить длину пароля", callback_data="set_password_length")
    button_info = InlineKeyboardButton("Информация о боте", url="https://telegra.ph/School-Project-11-21", callback_data="Information about the Creator")
    keyboard.row(button_do_generate, button_set_value)
    keyboard.add(button_info)
    return keyboard
