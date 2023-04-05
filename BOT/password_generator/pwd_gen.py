import string
import secrets

class PasswordGenerator:

    def __init__(self, length=16):
        self.length = min(length, 100)

    def generate_password(self):
        letters_upper = string.ascii_uppercase
        letters_lower = string.ascii_lowercase
        digits = string.digits
        symbols = string.punctuation

        # Concatenate all the possible characters
        all_chars = letters_upper + letters_lower + digits + symbols

        # Generate a random password
        password = ''.join(secrets.choice(all_chars) for i in range(self.length))

        return password

