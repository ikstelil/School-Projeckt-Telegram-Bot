from .start_handler import start_handler
from .password_handler import generate_password_handler, set_password_length_handler, process_password_length_message

def register_handlers(dp):
    dp.register_message_handler(start_handler, commands='start')
    dp.register_callback_query_handler(generate_password_handler, lambda c: c.data == 'generate_password')
    dp.register_callback_query_handler(set_password_length_handler, lambda c: c.data == 'set_password_length')
    dp.register_message_handler(process_password_length_message)
