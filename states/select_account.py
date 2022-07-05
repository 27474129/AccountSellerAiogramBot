from aiogram.dispatcher.filters.state import State, StatesGroup


class SelectAccount(StatesGroup):
    choice_of_company_name = State()

    steam_company_games = State()

    # games
    dota2 = State()
    csgo = State()
    gta5 = State()
    # end games
    select_price = State()