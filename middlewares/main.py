from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types


class MainMiddleware(BaseMiddleware):
    async def on_pre_process_callback_query(self, callback : types.CallbackQuery, data: dict):
        await callback.answer()