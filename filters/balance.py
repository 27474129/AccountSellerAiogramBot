from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class Balance(BoundFilter):
    async def check(self, callback : types.CallbackQuery):
        callback_data = callback.data
        if (
            callback_data == "<10" or callback_data == "11-30" or
            callback_data == "31-55" or callback_data == "60-80" or
            callback_data == ">100" or callback_data == "200"
        ):
            return True