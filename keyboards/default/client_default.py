from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

class SteamClientDefault:
    def __init__(self):
        self.back_button = KeyboardButton("Назад")

    def set_filter_keyboard(self):
        confirm_button = KeyboardButton("Подтвердить фильтр")

        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(confirm_button)
        keyboard.add(self.back_button)
        return keyboard
