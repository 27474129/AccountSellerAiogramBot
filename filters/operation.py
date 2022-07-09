from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class OperationFilter(BoundFilter):
    async def check(self, callback : types.CallbackQuery):
        callback_data = callback.data
        if (
            callback_data == "decency" or callback_data == "dota_hours" or
            callback_data == "lvl" or callback_data == "ratings" or
            callback_data == "ranks" or callback_data == "prime" or
            callback_data == "csgo_hours" or callback_data == "faceit" or
            callback_data == "balance" or callback_data == "char_lvl" or
            callback_data == "edition"
        ):
            return True