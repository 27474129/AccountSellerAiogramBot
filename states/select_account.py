from aiogram.dispatcher.filters.state import State, StatesGroup


class Select_account(StatesGroup):
    choice_of_company_name = State()

    steam_company = State()
    select_games = State()
    select_price = State()