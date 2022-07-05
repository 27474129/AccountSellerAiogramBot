from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class ClientInline:
    def __init__(self):
        self.back_button = InlineKeyboardButton(text="Назад", callback_data="back")


    def get_companies_keyboard(self):
        origin_button = InlineKeyboardButton(text="Origin", callback_data="Origin")
        steam_button = InlineKeyboardButton(text="Steam", callback_data="Steam")
        epic_games_button = InlineKeyboardButton(text="Epic Games", callback_data="Epic Games")
        blizzard_button = InlineKeyboardButton(text="Blizzard", callback_data="Blizzard")


        company_keyboard = InlineKeyboardMarkup(row_width=2)
        company_keyboard.add(origin_button, steam_button)
        company_keyboard.add(epic_games_button, blizzard_button)
        return company_keyboard



    def get_steam_games_keyboard(self):
        dota2_game_button = InlineKeyboardButton(text="Dota 2", callback_data="dota")
        csgo_game_button = InlineKeyboardButton(text="CS:GO", callback_data="csgo")
        gta5_game_button = InlineKeyboardButton(text="GTA 5", callback_data="gta5")


        games_keyboard = InlineKeyboardMarkup(row_width=3)
        games_keyboard.add(dota2_game_button, gta5_game_button, csgo_game_button)
        games_keyboard.add(self.back_button)

        return games_keyboard

    def get_dota_keyboard(self):
        prices = InlineKeyboardButton(text="Выбрать интервал цен", callback_data="prices")

        prices_keyboard = InlineKeyboardMarkup()
        prices_keyboard.add(prices)
        prices_keyboard.add(self.back_button)
        return prices_keyboard

    def get_prices_keyboard(self):
        prices_keyboard = InlineKeyboardMarkup()
        prices_keyboard.add(self.back_button)
