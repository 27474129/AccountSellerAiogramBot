from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class DotaClientInline:
    def __init__(self):
        self.back_button = InlineKeyboardButton(text="Назад", callback_data="back")


    def get_dota_keyboard(self, buttons_to_change):
        ratings_button = InlineKeyboardButton(text="Выбрать рейтинг в доте", callback_data="ratings")
        account_lvl_button = InlineKeyboardButton(text="Выбрать уровень в доте", callback_data="lvl")
        hours_button = InlineKeyboardButton(text="Выбрать количество часов в доте", callback_data="dota_hours")
        decency_button = InlineKeyboardButton(text="Выбрать уровень порядочности в доте", callback_data="decency")

        for buttons_to_change in buttons_to_change:
            if (buttons_to_change == "ratings"):
                ratings_button.text = "Рейтинг в доте уже выбран"
            if (buttons_to_change == "lvl"):
                account_lvl_button.text = "Уровень дота аккаунта уже выбран"
            if (buttons_to_change == "dota_hours"):
                hours_button.text = "Количество часов в доте уже выбранно"
            if (buttons_to_change == "decency"):
                decency_button.text = "Уровень порядочности уже установлен"


        dota_keyboard = InlineKeyboardMarkup()
        dota_keyboard.add(ratings_button)
        dota_keyboard.add(account_lvl_button)
        dota_keyboard.add(hours_button)
        dota_keyboard.add(decency_button)
        dota_keyboard.add(self.back_button)
        return dota_keyboard


    def get_dota_rating_sheet(self):
        rating1 = InlineKeyboardButton(text="Меньше 1000 mmr", callback_data="<1000")
        rating2 = InlineKeyboardButton(text="1000 - 2000 mmr", callback_data="1000-2000")
        rating3 = InlineKeyboardButton(text="2001 - 3000 mmr", callback_data="2001-3000")
        rating4 = InlineKeyboardButton(text="3001 - 4000 mmr", callback_data="3001-4000")
        rating5 = InlineKeyboardButton(text="4001 - 5000 mmr", callback_data="4001-5000")
        rating6 = InlineKeyboardButton(text="5001 - 6000 mmr", callback_data="5001-6000")
        rating7 = InlineKeyboardButton(text="6001 - 7000 mmr", callback_data="6001-7000")
        rating8 = InlineKeyboardButton(text="7000 - 8000 mmr", callback_data="7000-8000")

        rating_sheet_keyboard = InlineKeyboardMarkup()
        rating_sheet_keyboard.add(rating1, rating2)
        rating_sheet_keyboard.add(rating3, rating4)
        rating_sheet_keyboard.add(rating5, rating6)
        rating_sheet_keyboard.add(rating7, rating8)
        rating_sheet_keyboard.add(self.back_button)

        return rating_sheet_keyboard

    def get_dota_account_lvls_sheet(self):
        lvls1 = InlineKeyboardButton(text="Меньше 10 уровня", callback_data="<10")
        lvls2 = InlineKeyboardButton(text="11 - 20 уровни", callback_data="11-20")
        lvls3 = InlineKeyboardButton(text="21 - 35 уровни", callback_data="21-35")
        lvls4 = InlineKeyboardButton(text="36 - 50 уровни", callback_data="36-50")
        lvls5 = InlineKeyboardButton(text="51 - 65 уровни", callback_data="51-65")
        lvls6 = InlineKeyboardButton(text="Больше 66 уровня", callback_data=">66")

        lvls = InlineKeyboardMarkup()
        lvls.add(lvls1, lvls2)
        lvls.add(lvls3, lvls4)
        lvls.add(lvls5, lvls6)
        lvls.add(self.back_button)

        return lvls

    def get_dota_hours_sheet(self):
        hours1 = InlineKeyboardButton(text="Менее 500 часов", callback_data="<500")
        hours2 = InlineKeyboardButton(text="500 - 1000 часов", callback_data="501-1000")
        hours3 = InlineKeyboardButton(text="1000 - 1500 часов", callback_data="1001-1500")
        hours4 = InlineKeyboardButton(text="1500 - 2000 часов", callback_data="1501-2000")
        hours5 = InlineKeyboardButton(text="2000 - 3000 часов", callback_data="2001-3000")
        hours6 = InlineKeyboardButton(text="3000 - 4000 часов", callback_data="3001-4000")
        hours7 = InlineKeyboardButton(text="4000 - 5000 часов", callback_data="4001-5000")
        hours8 = InlineKeyboardButton(text="Более 5000 часов", callback_data=">5000")

        hours = InlineKeyboardMarkup()

        hours.add(hours1, hours2)
        hours.add(hours3, hours4)
        hours.add(hours5, hours6)
        hours.add(hours7, hours8)
        hours.add(self.back_button)

        return hours

    def get_dota_decency_sheet(self):
        decency1 = InlineKeyboardButton(text="Менее 3000 порядочности", callback_data="<3000")
        decency2 = InlineKeyboardButton(text="3000 - 5000 порядочности", callback_data="3001-5000")
        decency3 = InlineKeyboardButton(text="5000 - 7500 порядочности", callback_data="5001-7500")
        decency4 = InlineKeyboardButton(text="7500 - 10000 порядочности", callback_data="7501-10000")

        decency = InlineKeyboardMarkup()
        decency.add(decency1, decency2)
        decency.add(decency3, decency4)
        decency.add(self.back_button)

        return decency

