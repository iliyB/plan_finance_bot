import logging

from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.commands import CommandEnum
from bot.loader import dp
from bot.services.categories import CategoryService
from bot.states import FSMAddCategory

logger = logging.getLogger(__name__)


@dp.message_handler(commands=[CommandEnum.ADD_CATEGORY.value], state=None)
async def add_category_start(message: types.Message) -> None:
    await FSMAddCategory.command.set()
    await message.reply("Введите название категории")


@dp.message_handler(state=FSMAddCategory.command)
async def add_category_name(message: types.Message, state: FSMContext) -> None:
    await message.answer(await CategoryService.add_for_user(message.text, message.from_user.id))
    await message.answer(message.text)
    await state.finish()
