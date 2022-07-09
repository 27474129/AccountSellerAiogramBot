from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class CsgoClientInline:
    def __init__(self):
        self.back_button = InlineKeyboardButton(text="Назад", callback_data="back")

    def get_csgo_keyboard(self, buttons_to_change):
        ratings_button = InlineKeyboardButton(text="Выбрать звание в кс", callback_data="ranks")
        prime_status_button = InlineKeyboardButton(text="Указать наличие прайм статуса в кс", callback_data="prime")
        hours_button = InlineKeyboardButton(text="Выбрать количество часов в кс", callback_data="csgo_hours")
        faceit_lvl_button = InlineKeyboardButton(text="Выбрать уровень фейсита на аккаунте", callback_data="faceit")

        for buttons_to_change in buttons_to_change:
            if (buttons_to_change == "ranks"):
                ratings_button.text = "Звание в кс уже выбрано"
            if (buttons_to_change == "prime"):
                prime_status_button.text = "Наличие прайм статуса уже установлено"
            if (buttons_to_change == "csgo_hours"):
                hours_button.text = "Количество часов в кс уже выбранно"
            if (buttons_to_change == "faceit"):
                faceit_lvl_button.text = "Уровень фейсита уже выбран"


        dota_keyboard = InlineKeyboardMarkup()
        dota_keyboard.add(ratings_button)
        dota_keyboard.add(prime_status_button)
        dota_keyboard.add(hours_button)
        dota_keyboard.add(faceit_lvl_button)
        dota_keyboard.add(self.back_button)


        return dota_keyboard
    
    def get_csgo_ranks_keyboard(self):
        rank1 = InlineKeyboardButton(text="Серебро", callback_data="silver")
        rank2 = InlineKeyboardButton(text="Золотая звезда", callback_data="gold")
        rank3 = InlineKeyboardButton(text="Магистры (Калаши)", callback_data="ak")
        rank4 = InlineKeyboardButton(text="Большая звезда", callback_data="bigstar")
        rank5 = InlineKeyboardButton(text="Беркут", callback_data="eagle")
        rank6 = InlineKeyboardButton(text="Беркут с венками", callback_data="eagle2")
        rank7 = InlineKeyboardButton(text="Суприм", callback_data="supreme")
        rank8 = InlineKeyboardButton(text="Глобал", callback_data="global")

        csgo_ranks_keyboard = InlineKeyboardMarkup()
        csgo_ranks_keyboard.add(rank1, rank2)
        csgo_ranks_keyboard.add(rank3, rank4)
        csgo_ranks_keyboard.add(rank5, rank6)
        csgo_ranks_keyboard.add(rank7, rank8)

        csgo_ranks_keyboard.add(self.back_button)

        return csgo_ranks_keyboard

    def get_csgo_prime_keyboard(self):
        have_prime = InlineKeyboardButton(text="С праймом", callback_data="prime")
        havent_prime = InlineKeyboardButton(text="Без прайма", callback_data="not_prime")

        prime_keyboard = InlineKeyboardMarkup()
        prime_keyboard.add(have_prime)
        prime_keyboard.add(havent_prime)
        prime_keyboard.add(self.back_button)

        return prime_keyboard

    def get_csgo_faceit_keyboard(self):
        lvl1 = InlineKeyboardButton(text="1 - 3 уровень фейсита", callback_data="1-3")
        lvl2 = InlineKeyboardButton(text="4 - 6 уровень фейсита", callback_data="4-6")
        lvl3 = InlineKeyboardButton(text="7 - 8 уровень фейсита", callback_data="7-8")
        lvl4 = InlineKeyboardButton(text="9 уровень фейсита", callback_data="9")
        lvl5 = InlineKeyboardButton(text="10 уровень фейсита", callback_data="10")

        faceit_keyboard = InlineKeyboardMarkup()
        faceit_keyboard.add(self.back_button)
        faceit_keyboard.add(lvl1, lvl2)
        faceit_keyboard.add(lvl3, lvl4)
        faceit_keyboard.add(lvl5)
        faceit_keyboard.add(self.back_button)
        return faceit_keyboard