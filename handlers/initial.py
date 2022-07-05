from aiogram import types
from text import *
from loader import Loader
from keyboards.inline.client_inline import ClientInline
from states.select_account import SelectAccount
from aiogram.dispatcher import FSMContext




ld = Loader()
dp = ld.get_dispatcher()



@dp.message_handler(commands=["start"], state=None)
async def start_handler(message : types.Message):
    cl_inline = ClientInline()
    company_keyboard = cl_inline.get_companies_keyboard()
    await message.answer(f"Привет, {message.from_user.username}, {commands[ 'start' ]}", reply_markup=company_keyboard)
    await SelectAccount.choice_of_company_name.set()


@dp.callback_query_handler(text="Steam", state=SelectAccount.choice_of_company_name)
async def callback_steam(callback : types.CallbackQuery, state : FSMContext):
    cl_inline = ClientInline()
    steam_games_keyboard = cl_inline.get_steam_games_keyboard()
    await callback.answer()
    await callback.message.answer(text=f"{states[ 'steam_company_games' ]}", reply_markup=steam_games_keyboard)
    await SelectAccount.steam_company_games.set()




@dp.callback_query_handler(text="back", state="*")
async def cancel_state(callback : types.CallbackQuery, state : FSMContext):
    current_state = await state.get_state()
    cl_inline = ClientInline()
    await callback.answer()

    if (current_state == "SelectAccount:steam_company_games"):
        await state.set_state(SelectAccount.choice_of_company_name)
        company_keyboard = cl_inline.get_companies_keyboard()
        await callback.message.answer(f"{states['choice_of_company_name']}", reply_markup=company_keyboard)


