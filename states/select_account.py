from aiogram.dispatcher.filters.state import State, StatesGroup


class SelectAccount(StatesGroup):
    set_price = State()
    confirm_price = State()
    steam_games = State()
    # games
    dota = State()
    select_rating = State()
    set_rating = State()
    csgo = State()
    gta5 = State()
    # end games

    confirm_filter = State()

