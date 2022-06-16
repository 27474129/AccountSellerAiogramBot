from aiogram import types
from loader import Loader

ld = Loader()
dp = ld.get_dispatcher()


@dp.message_handler(commands=[ "start", "help" ])
async def initial_handler(message : types.Message):
    await message.answer("Hello")
