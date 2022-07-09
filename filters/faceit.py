from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class FaceitFilter(BoundFilter):
    async def check(self, callback : types.CallbackQuery):
        callback_data = callback.data
        if (
            callback_data == "1-3" or callback_data == "4-6" or
            callback_data == "7-8" or callback_data == "9" or
            callback_data == "10"
        ):
            return True
