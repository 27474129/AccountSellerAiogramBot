from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class GtaClientInline:
    def __init__(self):
        self.back_button = InlineKeyboardButton(text="Назад", callback_data="back")


    def get_gta_keyboard(self, buttons_to_change):
        balance_button = InlineKeyboardButton(text="Выбрать количество денег на аккаунте в gta online", callback_data="balance")
        char_lvl_button = InlineKeyboardButton(text="Выбрать уровень персонажа на аккаунте в gta online", callback_data="char_lvl")
        edition_button = InlineKeyboardButton(text="Выберите издание игры", callback_data="edition")


        for buttons_to_change in buttons_to_change:
            if (buttons_to_change == "balance"):
                balance_button.text = "Баланс на аккаунте в gta online уже установлен"
            if (buttons_to_change == "char_lvl"):
                char_lvl_button.text = "Уровень персонажа уже установлен"
            if (buttons_to_change == "edition"):
                edition_button.text = "Издание игры уже выбрано"


        gta_keyboard = InlineKeyboardMarkup()

        gta_keyboard.add(balance_button)
        gta_keyboard.add(char_lvl_button)
        gta_keyboard.add(edition_button)
        gta_keyboard.add(self.back_button)

        return gta_keyboard

    def get_gta_balance_keyboard(self):
        balance1 = InlineKeyboardButton(text="Меньше 10 миллионов", callback_data="<10")
        balance2 = InlineKeyboardButton(text="10 - 30 миллионов", callback_data="11-30")
        balance3 = InlineKeyboardButton(text="30 - 50 миллионов", callback_data="31-55")
        balance4 = InlineKeyboardButton(text="60 - 80 миллионов", callback_data="60-80")
        balance5 = InlineKeyboardButton(text="Больше 100 миллионов", callback_data=">100")
        balance6 = InlineKeyboardButton(text="200 миллионов", callback_data="200")

        gta_balance_keyboard = InlineKeyboardMarkup()

        gta_balance_keyboard.add(balance1, balance2)
        gta_balance_keyboard.add(balance3, balance4)
        gta_balance_keyboard.add(balance5, balance6)
        gta_balance_keyboard.add(self.back_button)

        return gta_balance_keyboard

    def get_gta_char_lvl_keyboard(self):
        lvl1 = InlineKeyboardButton(text="30 - 50 уровень", callback_data="30-50")
        lvl2 = InlineKeyboardButton(text="50 - 90 уровень", callback_data="51-90")
        lvl3 = InlineKeyboardButton(text="100 - 150 уровень", callback_data="100-150")
        lvl4 = InlineKeyboardButton(text="200 уровень и больше", callback_data=">200")

        gta_char_lvl_keyboard = InlineKeyboardMarkup()

        gta_char_lvl_keyboard.add(lvl1, lvl2)
        gta_char_lvl_keyboard.add(lvl3, lvl4)
        gta_char_lvl_keyboard.add(self.back_button)

        return gta_char_lvl_keyboard

    def get_gta_edition_keyboard(self):
        edition1 = InlineKeyboardButton(text="Special Edition", callback_data="special")
        edition2 = InlineKeyboardButton(text="Collector's Edition", callback_data="collectors")

        edition_keyboard = InlineKeyboardMarkup()

        edition_keyboard.add(edition1)
        edition_keyboard.add(edition2)
        edition_keyboard.add(self.back_button)

        return edition_keyboard
