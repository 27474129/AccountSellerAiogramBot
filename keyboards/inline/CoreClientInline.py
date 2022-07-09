from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class CoreClientInline:
    def __init__(self):
        self.back_button = InlineKeyboardButton(text="Назад", callback_data="back")

    def get_initial_keyboard(self):
        initial_button = InlineKeyboardButton(text="Начнём!", callback_data="start")

        initial_keyboard = InlineKeyboardMarkup()
        initial_keyboard.add(initial_button)
        return initial_keyboard

    def get_steam_games_keyboard(self):
        dota2_game_button = InlineKeyboardButton(text="Dota 2", callback_data="dota")
        csgo_game_button = InlineKeyboardButton(text="CS:GO", callback_data="csgo")
        gta5_game_button = InlineKeyboardButton(text="GTA V", callback_data="gta")

        games_keyboard = InlineKeyboardMarkup()
        games_keyboard.add(dota2_game_button, gta5_game_button, csgo_game_button)
        games_keyboard.add(self.back_button)

        return games_keyboard

    def get_prices_keyboard(self):
        price1 = InlineKeyboardButton(text="<1000 рублей", callback_data="<1000")
        price2 = InlineKeyboardButton(text="1000 - 2000 рублей", callback_data="1000-2000")
        price3 = InlineKeyboardButton(text="2001 - 3000 рублей", callback_data="2001-3000")
        price4 = InlineKeyboardButton(text="3001 - 4500 рублей", callback_data="3001-4500")
        price5 = InlineKeyboardButton(text="4501 - 6000 рублей", callback_data="4501-6000")
        price6 = InlineKeyboardButton(text="6001 - 8000 рублей", callback_data="6001-8000")
        price7 = InlineKeyboardButton(text="8000 - 9999 рублей", callback_data="8000-9999")
        price8 = InlineKeyboardButton(text=">10000 рублей", callback_data=">10000")


        prices_keyboard = InlineKeyboardMarkup()
        prices_keyboard.add(price1, price2)
        prices_keyboard.add(price3, price4)
        prices_keyboard.add(price5, price6)
        prices_keyboard.add(price7, price8)
        return prices_keyboard