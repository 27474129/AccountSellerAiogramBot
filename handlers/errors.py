from aiogram.types import Update
from loader import Loader

ld = Loader()
dp = ld.get_dispatcher()

@dp.errors_handler()
async def errors_handler(update, exception):
    print(exception)
    return True