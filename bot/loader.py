import os

from aiogram import Bot, types, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
# dp.middleware.setup(LoggingMiddleware())
