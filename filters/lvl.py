from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class AccountLvl(BoundFilter):
    async def check(self, callback : types.CallbackQuery):
        callback_data = callback.data
        if (
            callback_data == "<10" or callback_data == "11-20" or
            callback_data == "21-35" or callback_data == "36-50" or
            callback_data == "51-65" or callback_data == ">66"
        ):
            return True
