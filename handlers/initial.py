from aiogram import types
from text import *
from loader import Loader
from keyboards.inline.client_inline import Client_inline
from states.select_account import Select_account
from aiogram.dispatcher import FSMContext



ld = Loader()
dp = ld.get_dispatcher()



@dp.message_handler(commands=["start"], state=None)
async def start_handler(message : types.Message):
    cl_inline = Client_inline()
    company_keyboard = cl_inline.get_company_keyboard()
    await message.answer(f"Привет, {message.from_user.username}, {commands[ 'start' ]}", reply_markup=company_keyboard)
    await Select_account.choice_of_company_name.set()


@dp.callback_query_handler(text="Steam", state=Select_account.choice_of_company_name)
async def callback_steam(callback : types.CallbackQuery, state : FSMContext):
    cl_inline = Client_inline()
    steam_categories_keyboard = cl_inline.get_steam_categories_keyboard()
    await callback.answer()
    await callback.message.answer(text=f"{states[ 'steam_company' ]}", reply_markup=steam_categories_keyboard)
    await Select_account.steam_company.set()




@dp.callback_query_handler(text="back", state="*")
async def cancel_state(callback : types.CallbackQuery, state : FSMContext):
    current_state = await state.get_state()
    cl_inline = Client_inline()
    await callback.answer()
    if (current_state is None):
        return

    if (current_state == "Select_account:steam_company"):
        await state.set_state(Select_account.choice_of_company_name)
        company_keyboard = cl_inline.get_company_keyboard()
        await callback.message.answer(f"{states['choice_of_company_name']}", reply_markup=company_keyboard)

    if (current_state == "Select_account:select_games"):
        await state.set_state(Select_account.steam_company)
        steam_categories_keyboard = cl_inline.get_steam_categories_keyboard()
        await callback.message.answer(text=f"{states[ 'steam_company' ]}", reply_markup=steam_categories_keyboard)
