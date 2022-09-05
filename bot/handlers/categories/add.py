from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.bot import bot, dp
from bot.commands import CommandEnum
from bot.services.categories import CategoryService
from bot.states import FSMAddCategory


@dp.callback_query_handler(
    lambda c: c.data == CommandEnum.ADD_CATEGORY.value, state=None
)
async def add_category_start(callback_query: types.CallbackQuery) -> None:
    await FSMAddCategory.command.set()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Введите название категории")
    await bot.delete_message(
        callback_query.from_user.id, callback_query.message.message_id
    )


@dp.message_handler(state=FSMAddCategory.command)
async def add_category_name(message: types.Message, state: FSMContext) -> None:
    await CategoryService.add_for_user(message.text, message.from_user.id)
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.send_message(message.from_user.id, f"Категория {message.text} добавлена")
    await state.finish()
