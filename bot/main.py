from aiogram.utils import executor

# from loguru import logger
from bot import loggers

if __name__ == "__main__":
    # logger.add("logs/logs.log", format="{time} {level} {message}", level="DEBUG", rotation="1 MB", compression="zip")
    # logger.disable("sqlalchemy.engine.Engine")
    import logging

    import middlewares
    from handlers import dp

    # logging.basicConfig(level=logging.DEBUG)
    # logging.getLogger("sqlalchemy.engine.Engine").setLevel(logging.WARNING)
    middlewares.setup(dp)
    loggers.setup()
    executor.start_polling(dp, skip_updates=True)
