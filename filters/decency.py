from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class AccountDecency(BoundFilter):
    async def check(self, callback : types.CallbackQuery):
        callback_data = callback.data
        if (
            callback_data == "<3000" or callback_data == "3001-5000" or
            callback_data == "5001-7500" or callback_data == "5001-7500" or
            callback_data == "7501-10000"
        ):
            return True