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
    set_csgo_rank = State()
    set_csgo_hours = State()
    set_csgo_faceit = State()
    set_csgo_prime = State()
    gta = State()
    set_gta_char_lvl = State()
    set_gta_balance = State()
    set_gta_edition = State()
    # end games

    confirm_filter = State()
