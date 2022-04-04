import logging

from aiogram import types

from bot.loader import dp

logger = logging.getLogger(__name__)


@dp.message_handler(commands=["categories"])
async def list_categories(message: types.Message) -> None:
    await message.answer("categories")
    await message.answer(message.user)
