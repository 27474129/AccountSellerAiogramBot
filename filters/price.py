from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class PriceFilter(BoundFilter):
    async def check(self, callback : types.CallbackQuery):
        callback_data = callback.data
        if (
            callback_data == "<1000" or callback_data == "1000-2000" or
            callback_data == "2001-3000" or callback_data == "3001-4500" or
            callback_data == "4501-6000" or callback_data == "6001-8000" or
            callback_data == "8000-9999" or callback_data == ">10000"
        ):
            return True

