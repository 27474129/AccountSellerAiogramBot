from loader import Loader
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.select_account import Select_account
from keyboards.inline.client_inline import Client_inline
from text import *


ld = Loader()
dp = ld.get_dispatcher()

@dp.callback_query_handler(text="game_selection", state=Select_account.steam_company)
async def game_selection(callback : types.CallbackQuery):
    cl_inline = Client_inline()
    games_keyboard = cl_inline.get_games_keyboard()
    await callback.message.answer(f"{states[ 'select_games' ]}", reply_markup=games_keyboard)
    await Select_account.select_games.set()