from aiogram import types
from text import *
from loader import Loader
from keyboards.inline.client_inline import SteamClientInline
from states.select_account import SelectAccount
from aiogram.dispatcher import FSMContext
from keyboards.default.client_default import SteamClientDefault
from aiogram.dispatcher import filters
from filters.price import PriceFilter

import functions



ld = Loader()
cl_inline = SteamClientInline()
cl_default = SteamClientDefault()
dp = ld.get_dispatcher()



@dp.message_handler(commands=["start", "help"])
async def initial_handler(message : types.Message):
    initial_keyboard = cl_inline.get_initial_keyboard()
    await message.answer(f"Привет, {message.from_user.username}, {commands[ 'start' ]}", reply_markup=initial_keyboard)


@dp.callback_query_handler(text="start")
async def select_price(callback : types.CallbackQuery, state : FSMContext):
    prices_keyboard = cl_inline.get_prices_keyboard()
    await callback.answer()
    await callback.message.answer(text=f"{states[ 'select_price' ]}", reply_markup=prices_keyboard)
    await SelectAccount.set_price.set()




@dp.callback_query_handler(PriceFilter(), state=SelectAccount.set_price)
async def set_price(callback : types.CallbackQuery, state : FSMContext):
    await callback.answer()
    set_price_keyboard = cl_default.set_filter_keyboard()


    async with state.proxy() as data:
        data[ "price" ] = callback.data

    await callback.message.answer(f"{states[ 'confirm_filter' ]}", reply_markup=set_price_keyboard)
    await SelectAccount.confirm_price.set()


@dp.message_handler(filters.Text(equals="Подтвердить фильтр"), state=SelectAccount.confirm_price)
@dp.message_handler(filters.Text(equals="Назад"), state=SelectAccount.confirm_price)
async def confirm_price(message : types.Message, state : FSMContext):
    if (message.text == "Подтвердить фильтр"):
        steam_games_keyboard = cl_inline.get_steam_games_keyboard()
        await message.answer("Фильтр успешно установлен")
        await message.answer(f"{states['steam_games']}", reply_markup=steam_games_keyboard)
        await state.set_state(SelectAccount.steam_games)
    else:
        prices_keyboard = cl_inline.get_prices_keyboard()
        await message.answer(text=f"{states[ 'select_price' ]}", reply_markup=prices_keyboard)
        await state.set_state(SelectAccount.set_price)

        async with state.proxy() as data:
            del data[ "price" ]



@dp.message_handler(filters.Text(equals="Назад"), state=SelectAccount.confirm_filter)
@dp.message_handler(filters.Text(equals="Подтвердить фильтр"), state=SelectAccount.confirm_filter)
async def confirm_filter(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        current_game = data[ "current_game" ]
        current_operation = data[ "current_operation" ]


        if (message.text == "Подтвердить фильтр"):
            await message.answer("Фильтр установлен!")
            data[ "filtered" ].append( f"{current_operation}" )
            game_keyboard = functions.get_keyboard(current_game, data["filtered"])
        else:
            await message.answer("Установка фильтра отменена")

            del data[ "current_operation" ]
            if (len(data[ "filtered" ]) != 0):
                data[ "filtered" ].remove(f"{current_operation}")

            game_keyboard = functions.get_keyboard(current_game, [])


    await message.answer(f"{states[ f'{current_game}' ]}", reply_markup=game_keyboard)
    await functions.back_from_select_state(state)



@dp.callback_query_handler(text="back", state="*")
async def change_state(callback : types.CallbackQuery, state : FSMContext):
    await callback.answer()
    current_state = await state.get_state()
    games = ["gta5", "dota", "csgo"]

    for game in games:
        if (current_state == f"SelectAccount:{game}"):
            await state.set_state(SelectAccount.steam_games)
            steam_games_keyboard = cl_inline.get_steam_games_keyboard()
            await callback.message.answer(f"{states[ 'steam_games' ]}", reply_markup=steam_games_keyboard)

    if (current_state == "SelectAccount:steam_games"):
        await state.set_state(SelectAccount.set_price)
        prices_keyboard = cl_inline.get_prices_keyboard()
        await callback.message.answer(f"{states[ 'select_price' ]}", reply_markup=prices_keyboard)

    if (current_state == "SelectAccount:set_rating"):
        await functions.back_from_select_state(state)
        async with state.proxy() as data:
            current_game = data[ "current_game" ]
            del data[ "current_operation" ]
        game_keyboard = functions.get_keyboard(current_game, [])
        await callback.message.answer(f"{states[ 'dota' ]}", reply_markup=game_keyboard)

