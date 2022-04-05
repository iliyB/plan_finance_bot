import logging

from aiogram import types

from bot.commands import CommandEnum
from bot.loader import dp
from bot.services.categories import CategoryService

logger = logging.getLogger(__name__)


@dp.message_handler(commands=[CommandEnum.LIST_CATEGORY.value])
async def list_categories(message: types.Message) -> None:
    categories = await CategoryService.all_for_user(message.from_user.id)
    if categories:
        await message.answer(categories)
    else:
        await message.answer("У вас ещё нет категорий")
