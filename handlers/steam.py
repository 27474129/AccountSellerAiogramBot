from loader import Loader
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.select_account import SelectAccount
from keyboards.inline.client_inline import ClientInline
from text import *


ld = Loader()
dp = ld.get_dispatcher()



@dp.callback_query_handler(text="dota", state=SelectAccount.steam_company_games)
async def dota(callback : types.CallbackQuery, state : FSMContext):
    cl_inline = ClientInline()
    inline_keyboard = cl_inline.get_dota_keyboard()
    await callback.answer()
    await callback.message.answer(text=f"{states[ 'steam_company_games' ]}", reply_markup=inline_keyboard)
    await SelectAccount.dota2.set()


@dp.callback_query_handler(text="prices", state=SelectAccount.dota2)
async def prices(callback : types.CallbackQuery, state : FSMContext):
    await callback.answer()

    cl_inline = ClientInline()
    keyboard = cl_inline.get_prices_keyboard()
    await callback.message.answer(f"{states[ 'dota2' ]}", reply_markup=keyboard)
    await SelectAccount.select_price.set()


@dp.message_handler(state=SelectAccount.select_price)
async def get_price(message : types.Message):
    msg = message.text

