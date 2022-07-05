from loader import Loader
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.select_account import SelectAccount
from keyboards.inline.client_inline import SteamClientInline
from text import *
from aiogram.dispatcher import filters


ld = Loader()
dp = ld.get_dispatcher()



@dp.callback_query_handler(text="dota", state=SelectAccount.steam_company_games)
async def dota(callback : types.CallbackQuery, state : FSMContext):
    cl_inline = SteamClientInline()
    inline_keyboard = cl_inline.get_dota_keyboard()
    await callback.answer()
    await callback.message.answer(text=f"{states[ 'dota2' ]}", reply_markup=inline_keyboard)

    async with state.proxy() as data:
        data[ "current_game" ] = "dota2"
    await SelectAccount.dota2.set()


@dp.callback_query_handler(text="prices", state=SelectAccount.dota2)
async def prices(callback : types.CallbackQuery, state : FSMContext):
    await callback.answer()

    cl_inline = SteamClientInline()
    keyboard = cl_inline.get_prices_keyboard()
    await callback.message.answer(f"{states[ 'select_price' ]}", reply_markup=keyboard)
    await SelectAccount.select_price.set()
