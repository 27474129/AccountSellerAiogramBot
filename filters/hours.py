from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class AccountHours(BoundFilter):
    async def check(self, callback : types.CallbackQuery):
        callback_data = callback.data
        if (
            callback_data == "<500" or callback_data == "501-1000" or
            callback_data == "1001-1500" or callback_data == "1501-2000" or
            callback_data == "2001-3000" or callback_data == "3001-4000" or
            callback_data == "4001-5000" or callback_data == ">5000"
        ):
            return True
