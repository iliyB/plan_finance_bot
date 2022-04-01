from aiogram.utils import executor
from loguru import logger

if __name__ == "__main__":
    import middlewares
    from handlers import dp

    # logger.add("logs/logs.log", format="{time} {level} {message}", level="DEBUG", serialize=True)

    middlewares.setup(dp)
    executor.start_polling(dp, skip_updates=True)
