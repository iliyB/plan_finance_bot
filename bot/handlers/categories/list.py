import logging

from aiogram import types

from bot.commands import CommandEnum
from bot.loader import bot, dp
from bot.services.categories import CategoryService

logger = logging.getLogger(__name__)


@dp.callback_query_handler(lambda c: c.data == CommandEnum.LIST_CATEGORY.value)
async def list_categories(callback_query: types.CallbackQuery) -> None:
    categories = await CategoryService.all_for_user(callback_query.from_user.id)
    if categories:
        await bot.send_message(callback_query.from_user.id, categories)
    else:
        await bot.send_message(callback_query.from_user.id, "У вас ещё нет категорий")

    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
