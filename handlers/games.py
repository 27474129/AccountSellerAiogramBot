from loader import Loader
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.SelectAccount import SelectAccount
from keyboards.inline.DotaClientInline import DotaClientInline
from keyboards.default.ClientDefault import SteamClientDefault
from text import *
from aiogram.dispatcher import filters
from filters.rating import RatingFilter
from filters.lvl import AccountLvl
from filters.hours import AccountHours
from filters.decency import AccountDecency
from filters.operation import OperationFilter
from filters.ranks import RanksFilter
from filters.faceit import FaceitFilter
from filters.char_lvl import CharLvl
from filters.balance import Balance
import functions



ld = Loader()
dp = ld.get_dispatcher()
dota_inline = DotaClientInline()
cl_default = SteamClientDefault()



@dp.callback_query_handler(OperationFilter(), state=SelectAccount.gta)
@dp.callback_query_handler(OperationFilter(), state=SelectAccount.csgo)
@dp.callback_query_handler(OperationFilter(), state=SelectAccount.dota)
async def select_game_filter(callback : types.CallbackQuery, state : FSMContext):
    current_filter = callback.data
    async with state.proxy() as data:
        current_game = data[ "current_game" ]

    filter_sheet_keyboard = await functions.get_filter_keyboard_and_set_filter_state(current_filter, current_game)
    await callback.message.answer(f"{states[ f'select_{current_filter}' ]}", reply_markup=filter_sheet_keyboard)

    async with state.proxy() as data:
        data[ "current_operation" ] = current_filter




@dp.callback_query_handler(text="special", state=SelectAccount.set_gta_edition)
@dp.callback_query_handler(text="collectors", state=SelectAccount.set_gta_edition)
@dp.callback_query_handler(Balance(), state=SelectAccount.set_gta_balance)
@dp.callback_query_handler(CharLvl(), state=SelectAccount.set_gta_char_lvl)
@dp.callback_query_handler(state=SelectAccount.set_csgo_prime)
@dp.callback_query_handler(FaceitFilter(), state=SelectAccount.set_csgo_faceit)
@dp.callback_query_handler(RanksFilter(), state=SelectAccount.set_csgo_rank)
@dp.callback_query_handler(AccountHours(), state=SelectAccount.set_csgo_hours)
@dp.callback_query_handler(AccountDecency(), state=SelectAccount.set_dota_decency)
@dp.callback_query_handler(AccountHours(), state=SelectAccount.set_dota_hours)
@dp.callback_query_handler(AccountLvl(), state=SelectAccount.set_dota_account_lvl)
@dp.callback_query_handler(RatingFilter(), state=SelectAccount.set_dota_rating)
async def set_game_filter(callback : types.CallbackQuery, state : FSMContext):
    async with state.proxy() as data:
        filters = [
            "ratings", "dota_hours", "lvl", "decency",
            "csgo_hours", "prime", "faceit", "ranks",
            "char_lvl", "edition", "balance"
        ]

        for filter in filters:
            if (data[ "current_operation" ] == filter):

                data[ f"{filter}" ] = callback.data


    set_filter_keyboard = cl_default.set_filter_keyboard()


    await callback.message.answer("Подтвердите установку фильтра", reply_markup=set_filter_keyboard)
    await SelectAccount.confirm_filter.set()
