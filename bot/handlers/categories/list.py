import logging

from aiogram import types

from bot.commands import CommandEnum
from bot.keyboards.categories import create_retrieve_category_keyboard
from bot.loader import bot, dp
from bot.services.categories import CategoryService
from bot.states import FSMCategory

logger = logging.getLogger(__name__)


@dp.callback_query_handler(lambda c: c.data == CommandEnum.LIST_CATEGORY.value, state=None)
async def list_categories(callback_query: types.CallbackQuery) -> None:
    categories = await CategoryService.all_for_user(callback_query.from_user.id)
    if categories:
        await FSMCategory.categories.set()
        await bot.send_message(
            callback_query.from_user.id, "Ваши категории", reply_markup=create_retrieve_category_keyboard(categories)
        )
    else:
        await bot.send_message(callback_query.from_user.id, "У вас ещё нет категорий")

    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
