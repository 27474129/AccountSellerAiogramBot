from aiogram.dispatcher.filters.state import State, StatesGroup


class SelectAccount(StatesGroup):
    set_price = State()
    confirm_price = State()
    steam_games = State()
    # games
    dota = State()
    set_dota_rating = State()
    set_dota_account_lvl = State()
    set_dota_hours = State()
    set_dota_decency = State()

    csgo = State()
    gta5 = State()
    # end games

    confirm_filter = State()
