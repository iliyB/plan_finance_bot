from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.commands import CommandEnum
from bot.loader import bot, dp
from bot.services.categories import CategoryService
from bot.states import FSMCategory


@dp.callback_query_handler(lambda c: c.data == CommandEnum.DEL_CATEGORY.value, state=FSMCategory.category)
async def delete_category(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    async with state.proxy() as data:
        category_name = data.get("category_name")

    await CategoryService.delete_for_user(category_name, callback_query.from_user.id)
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, f"Категория {category_name} удалена")
    await state.finish()
