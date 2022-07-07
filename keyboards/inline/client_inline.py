from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class SteamClientInline:
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
        gta5_game_button = InlineKeyboardButton(text="GTA V", callback_data="gta5")


        games_keyboard = InlineKeyboardMarkup()
        games_keyboard.add(dota2_game_button, gta5_game_button, csgo_game_button)
        games_keyboard.add(self.back_button)

        return games_keyboard

    def get_dota_keyboard(self, buttons_to_change):
        ratings_button = InlineKeyboardButton(text="Выбрать рейтинг", callback_data="ratings")


        for buttons_to_change in buttons_to_change:
            if (buttons_to_change == "ratings"):
                ratings_button.text = "Рейтинг уже выбран"

        dota2_keyboard = InlineKeyboardMarkup()
        dota2_keyboard.add(ratings_button)
        dota2_keyboard.add(self.back_button)
        return dota2_keyboard



    def get_prices_keyboard(self):
        price1 = InlineKeyboardButton(text="<1000 rubles", callback_data="<1000")
        price2 = InlineKeyboardButton(text="1000 - 2000 rubles", callback_data="1000-2000")
        price3 = InlineKeyboardButton(text="2001 - 3000 rubles", callback_data="2001-3000")
        price4 = InlineKeyboardButton(text="3001 - 4500 rubles", callback_data="3001-4500")
        price5 = InlineKeyboardButton(text="4501 - 6000 rubles", callback_data="4501-6000")
        price6 = InlineKeyboardButton(text="6001 - 8000 rubles", callback_data="6001-8000")
        price7 = InlineKeyboardButton(text="8000 - 9999 rubles", callback_data="8000-9999")
        price8 = InlineKeyboardButton(text=">10000 rubles", callback_data=">10000")


        prices_keyboard = InlineKeyboardMarkup()
        prices_keyboard.add(price1, price2)
        prices_keyboard.add(price3, price4)
        prices_keyboard.add(price5, price6)
        prices_keyboard.add(price7, price8)
        return prices_keyboard

    def get_dota_rating_sheet(self):
        rating1 = InlineKeyboardButton(text="<1000 mmr", callback_data="<1000")
        rating2 = InlineKeyboardButton(text="1000 - 2000 mmr", callback_data="1000-2000")
        rating3 = InlineKeyboardButton(text="2001 - 3000 mmr", callback_data="2001-3000")
        rating4 = InlineKeyboardButton(text="3001 - 4000 mmr", callback_data="3001-4000")
        rating5 = InlineKeyboardButton(text="4001 - 5000 mmr", callback_data="4001-5000")
        rating6 = InlineKeyboardButton(text="5001 - 6000 mmr", callback_data="5001-6000")
        rating7 = InlineKeyboardButton(text="6001 - 7000 mmr", callback_data="6001-7000")
        rating8 = InlineKeyboardButton(text="7000 - 8000 mmr", callback_data="7000 - 8000")

        rating_sheet_keyboard = InlineKeyboardMarkup()
        rating_sheet_keyboard.add(rating1, rating2)
        rating_sheet_keyboard.add(rating3, rating4)
        rating_sheet_keyboard.add(rating5, rating6)
        rating_sheet_keyboard.add(rating7, rating8)
        rating_sheet_keyboard.add(self.back_button)

        return rating_sheet_keyboard