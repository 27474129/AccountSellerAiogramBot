from loader import Loader
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.select_account import SelectAccount
from keyboards.inline.client_inline import SteamClientInline
from keyboards.default.client_default import SteamClientDefault
from text import *
from aiogram.dispatcher import filters
from filters.rating import RatingFilter


ld = Loader()
dp = ld.get_dispatcher()
cl_inline = SteamClientInline()
cl_default = SteamClientDefault()


@dp.callback_query_handler(text="dota", state=SelectAccount.steam_games)
async def dota(callback : types.CallbackQuery, state : FSMContext):
    await callback.answer()
    async with state.proxy() as data:
        data[ "current_game" ] = "dota"
        if ("is_need_to_recreate" not in data):
            data["filtered"] = []
        data["is_need_to_recreate"] = True

    if (len(data[ "filtered" ]) != 0):
        dota_keyboard = cl_inline.get_dota_keyboard(data["filtered"])
    else:
        dota_keyboard = cl_inline.get_dota_keyboard([])

    await callback.message.answer(text=f"{states[ 'dota' ]}", reply_markup=dota_keyboard)
    await SelectAccount.dota.set()



@dp.callback_query_handler(text="ratings", state=SelectAccount.dota)
async def select_dota_rating(callback : types.CallbackQuery, state : FSMContext):
    async with state.proxy() as data:
        data[ "current_operation" ] = "ratings"

    await callback.answer()
    rating_sheet_keyboard = cl_inline.get_dota_rating_sheet()
    await callback.message.answer(f"{states[ 'select_rating' ]}", reply_markup=rating_sheet_keyboard)
    await SelectAccount.set_rating.set()



@dp.callback_query_handler(RatingFilter(), state=SelectAccount.set_rating)
async def set_dota_rating(callback : types.CallbackQuery, state : FSMContext):
    await callback.answer()
    async with state.proxy() as data:
        data[ "dota_rating" ] = callback.data

    set_filter_keyboard = cl_default.set_filter_keyboard()
    await callback.message.answer(f"{states[ 'set_rating' ]}", reply_markup=set_filter_keyboard)
    await SelectAccount.confirm_filter.set()

