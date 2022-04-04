from aiogram.utils import executor

from bot import loggers

if __name__ == "__main__":
    import middlewares
    from handlers import dp

    middlewares.setup(dp)
    loggers.setup()
    executor.start_polling(dp, skip_updates=True)
