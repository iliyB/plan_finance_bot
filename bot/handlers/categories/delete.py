import logging

from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.commands import CommandEnum
from bot.loader import bot, dp
from bot.services.categories import CategoryService
from bot.states import FSMDelCategory

logger = logging.getLogger(__name__)


@dp.callback_query_handler(lambda c: c.data == CommandEnum.DEL_CATEGORY.value, state=None)
async def add_category_start(callback_query: types.CallbackQuery) -> None:
    await FSMDelCategory.command.set()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Введите название категории")
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)


@dp.message_handler(state=FSMDelCategory.command)
async def add_category_name(message: types.Message, state: FSMContext) -> None:
    await CategoryService.delete_for_user(message.text, message.from_user.id)
    await message.reply("OK")
    await state.finish()
