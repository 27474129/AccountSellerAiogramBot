from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class CharLvl(BoundFilter):
    async def check(self, callback : types.CallbackQuery):
        callback_data = callback.data
        if (
            callback_data == "30-50" or callback_data == "51-90" or
            callback_data == "100-150" or callback_data == ">200"
        ):
            return True