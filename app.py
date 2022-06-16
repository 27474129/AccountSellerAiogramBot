if __name__ == "__main__":
    from aiogram import executor
    from config import Config
    from loader import Loader
    from handlers import dp


    ld = Loader()
    bot = ld.get_bot()


    async def notify_about_launch(dp):
        await bot.send_message(chat_id=Config.ADMINS_ID[0], text="Bot has been launched")


    executor.start_polling(dp, skip_updates=True, on_startup=notify_about_launch)