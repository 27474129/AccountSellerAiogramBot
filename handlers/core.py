from aiogram import types
from text import *
from loader import Loader
from keyboards.inline.client_inline import SteamClientInline
from states.select_account import SelectAccount
from aiogram.dispatcher import FSMContext
from keyboards.default.client_default import SteamClientDefault
from aiogram.dispatcher import filters

import functions


ld = Loader()
cl_inline = SteamClientInline()
cl_default = SteamClientDefault()
dp = ld.get_dispatcher()


@dp.message_handler(commands=["start"])
async def initial_handler(message : types.Message):
    initial_keyboard = cl_inline.get_initial_keyboard()
    await message.answer(f"Привет, {message.from_user.username}, {commands[ 'start' ]}", reply_markup=initial_keyboard)


@dp.callback_query_handler(text="start")
async def callback_steam(callback : types.CallbackQuery, state : FSMContext):
    cl_inline = SteamClientInline()
    steam_games_keyboard = cl_inline.get_steam_games_keyboard()
    await callback.answer()
    await callback.message.answer(text=f"{states[ 'steam_company_games' ]}", reply_markup=steam_games_keyboard)
    await SelectAccount.steam_company_games.set()



@dp.callback_query_handler(text="back", state="*")
async def change_state(callback : types.CallbackQuery, state : FSMContext):
    current_state = await state.get_state()
    await callback.answer()
    games = ["gta5", "dota2", "csgo"]


    if (current_state == "SelectAccount:steam_company_games"):
        await state.set_state(SelectAccount.choice_of_company_name)
        company_keyboard = cl_inline.get_initial_keyboard()
        await callback.message.answer(f"{states['choice_of_company_name']}", reply_markup=company_keyboard)


    for game in games:
        if (current_state == f"SelectAccount:{game}"):
            await state.set_state(SelectAccount.steam_company_games)
            steam_keyboard = cl_inline.get_steam_games_keyboard()
            await callback.message.answer(f"{states[ 'steam_company_games' ]}", reply_markup=steam_keyboard)


    if (current_state == "SelectAccount:select_price"):
        await functions.back_from_select_price_state(state)
        async with state.proxy() as data:
            current_game = data[ "current_game" ]

        keyboard = functions.get_keyboard(current_game)

        await callback.message.answer(f"{states[ f'{current_game}' ]}", reply_markup=keyboard)


@dp.callback_query_handler(text="<1000", state=SelectAccount.select_price)
@dp.callback_query_handler(text="1000-2000", state=SelectAccount.select_price)
@dp.callback_query_handler(text="2001-3000", state=SelectAccount.select_price)
@dp.callback_query_handler(text="3001-4500", state=SelectAccount.select_price)
@dp.callback_query_handler(text="4501-6000", state=SelectAccount.select_price)
@dp.callback_query_handler(text="6001-8000", state=SelectAccount.select_price)
@dp.callback_query_handler(text="8000-9999", state=SelectAccount.select_price)
@dp.callback_query_handler(text=">10000", state=SelectAccount.select_price)
async def set_price(callback : types.CallbackQuery, state : FSMContext):
    await callback.answer()
    keyboard = cl_default.set_price_keyboard()

    price = callback.message.text
    async with state.proxy() as data:
        data[ "price" ] = price

    await callback.message.answer(f"{states[ 'confirm_filter' ]}", reply_markup=keyboard)
    await SelectAccount.confirm_filter.set()


@dp.message_handler(filters.Text(equals="Подтвердить фильтр"), state=SelectAccount.confirm_filter)
async def confirm_filter(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        current_game = data[ "current_game" ]

    keyboard = functions.get_keyboard(current_game)
    await message.answer("Фильтр установлен!", reply_markup=types.ReplyKeyboardRemove())
    await message.answer(f"{states[ f'{current_game}' ]}", reply_markup=keyboard)
    await functions.back_from_select_price_state(state)