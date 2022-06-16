from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import Config
import asyncio


class Loader:
    __storage = MemoryStorage()
    __bot = Bot(Config.BOT_TOKEN, parse_mode="HTML")
    __dp = Dispatcher(__bot, storage=__storage, loop=asyncio.get_event_loop())



    def get_dispatcher(self):
        return self.__dp


    def get_bot(self):
        return self.__bot