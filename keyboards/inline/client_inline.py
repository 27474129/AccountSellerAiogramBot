from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Client_inline:
    def get_company_keyboard(self):
        self.__origin_button = InlineKeyboardButton(text="Origin", callback_data="Origin")
        self.__steam_button = InlineKeyboardButton(text="Steam", callback_data="Steam")
        self.__epic_games_button = InlineKeyboardButton(text="Epic Games", callback_data="Epic Games")
        self.__blizzard_button = InlineKeyboardButton(text="Blizzard", callback_data="Blizzard")


        self.__company_keyboard = InlineKeyboardMarkup(row_width=2)
        self.__company_keyboard.add(self.__origin_button, self.__steam_button)
        self.__company_keyboard.add(self.__epic_games_button, self.__blizzard_button)
        return self.__company_keyboard


    def get_steam_categories_keyboard(self):
        self.__game_selection_button = InlineKeyboardButton(text="Выбор игр", callback_data="game_selection")
        self.__price_selection_button = InlineKeyboardButton(text="Выбор ценовой категории", callback_data="price_selection")

        self.__search_accounts_button = InlineKeyboardButton(text="Поиск аккаунтов", callback_data="search_accounts")
        self.__back_button = InlineKeyboardButton(text="Назад", callback_data="back")


        self.__categories_keyboard = InlineKeyboardMarkup(row_width=2)

        self.__categories_keyboard.add(self.__price_selection_button, self.__game_selection_button)
        self.__categories_keyboard.add(self.__search_accounts_button)
        self.__categories_keyboard.add(self.__back_button)
        return self.__categories_keyboard

    def get_games_keyboard(self):
        self.__dota2_game_button = InlineKeyboardButton(text="Dota 2", callback_data="dota")
        self.__csgo_game_button = InlineKeyboardButton(text="CS:GO", callback_data="csgo")
        self.__gta5_game_button = InlineKeyboardButton(text="GTA 5", callback_data="gta5")

        self.__back_button = InlineKeyboardButton(text="Назад", callback_data="back")


        self.__games_keyboard = InlineKeyboardMarkup(row_width=3)
        self.__games_keyboard.add(self.__dota2_game_button, self.__gta5_game_button, self.__csgo_game_button)
        self.__games_keyboard.add(self.__back_button)

        return self.__games_keyboard