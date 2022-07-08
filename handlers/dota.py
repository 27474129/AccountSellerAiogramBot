from loader import Loader
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.SelectAccount import SelectAccount
from keyboards.inline.ClientInline import ClientInline
from keyboards.default.client_default import SteamClientDefault
from text import *
from aiogram.dispatcher import filters
from filters.rating import RatingFilter
from filters.lvl import AccountLvl
from filters.hours import AccountHours
from filters.decency import AccountDecency

import functions


ld = Loader()
dp = ld.get_dispatcher()
cl_inline = ClientInline()
cl_default = SteamClientDefault()



@dp.callback_query_handler(text="decency", state=SelectAccount.dota)
@dp.callback_query_handler(text="hours", state=SelectAccount.dota)
@dp.callback_query_handler(text="lvl", state=SelectAccount.dota)
@dp.callback_query_handler(text="ratings", state=SelectAccount.dota)
async def select_dota_filter(callback : types.CallbackQuery, state : FSMContext):
    current_filter = callback.data


    filter_sheet_keyboard = await functions.get_filter_keyboard_and_set_filter_state(current_filter)
    await callback.message.answer(f"{states[ f'select_dota_{current_filter}' ]}", reply_markup=filter_sheet_keyboard)

    async with state.proxy() as data:
        data[ "current_operation" ] = "dota_" + current_filter

@dp.callback_query_handler(AccountDecency(), state=SelectAccount.set_dota_decency)
@dp.callback_query_handler(AccountHours(), state=SelectAccount.set_dota_hours)
@dp.callback_query_handler(AccountLvl(), state=SelectAccount.set_dota_account_lvl)
@dp.callback_query_handler(RatingFilter(), state=SelectAccount.set_dota_rating)
async def set_dota_filter(callback : types.CallbackQuery, state : FSMContext):
    async with state.proxy() as data:
        filters = ["ratings", "hours", "lvl", "decency"]

        for filter in filters:

            if (data[ "current_operation" ] == "dota_" + filter):

                data[ f"dota_{filter}" ] = callback.data


    set_filter_keyboard = cl_default.set_filter_keyboard()


    await callback.message.answer("Подтвердите установку фильтра", reply_markup=set_filter_keyboard)
    await SelectAccount.confirm_filter.set()
