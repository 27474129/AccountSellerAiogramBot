from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class RanksFilter(BoundFilter):
    async def check(self, callback : types.CallbackQuery):
        callback_data = callback.data
        if (
            callback_data == "silver" or callback_data == "gold" or
            callback_data == "ak" or callback_data == "bigstar" or
            callback_data == "eagle" or callback_data == "eagle2" or
            callback_data == "supreme" or callback_data == "global"
        ):
            return True
