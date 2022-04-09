from aiogram import types

from bot.commands import CommandEnum
from bot.keyboards.tasks import my_tasks_keyboard
from bot.loader import bot, dp


@dp.callback_query_handler(lambda c: c.data == CommandEnum.LIST_TASK.value)
async def task_list(callback_query: types.CallbackQuery) -> None:
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, "Выберите промежуток времени", reply_markup=my_tasks_keyboard)
