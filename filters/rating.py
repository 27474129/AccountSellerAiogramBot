from aiogram.dispatcher.filters import BoundFilter
from aiogram import types

class RatingFilter(BoundFilter):
    async def check(self, callback : types.CallbackQuery):
        callback_data = callback.data
        if (
            callback_data == "<1000" or callback_data == "1000-2000" or
            callback_data == "2001-3000" or callback_data == "3001-4000" or
            callback_data == "4001-5000" or callback_data == "5001-6000" or
            callback_data == "6001-7000" or callback_data == "7000-8000"
        ):
            return True