from aiogram import types

from bot.commands import CommandEnum
from bot.keyboards.tasks import tasks_keyboard
from bot.loader import bot, dp


@dp.message_handler(commands=CommandEnum.TASK_KEYBOARD.name.lower())
async def task_keyboard_view(message: types.Message) -> None:
    await message.answer("Меню задач", reply_markup=tasks_keyboard)
    await bot.delete_message(message.from_user.id, message.message_id)
