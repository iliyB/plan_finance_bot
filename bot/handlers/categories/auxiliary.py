from aiogram import types

from bot.commands import CommandEnum
from bot.keyboards.categories import categories_keyboard
from bot.loader import bot, dp


@dp.message_handler(commands=[CommandEnum.CATEGORY_KEYBOARD.value])
async def category_keyboard_view(message: types.Message) -> None:
    await message.answer("Category", reply_markup=categories_keyboard)
    await bot.delete_message(message.from_user.id, message.message_id)
