import re

from aiogram import types

from bot.loader import bot, dp
from bot.services.categories import CategoryService


@dp.callback_query_handler(lambda c: re.match("category_[A-z0-9 _]*", c.data))
async def retrieve_category(callback_query: types.CallbackQuery) -> None:
    category = await CategoryService.get_by_name(callback_query.data.split("_")[-1])
    await bot.send_message(callback_query.from_user.id, category)
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
