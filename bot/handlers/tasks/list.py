from aiogram import types

from bot.commands import CommandEnum
from bot.keyboards.tasks import my_tasks_keyboard
from bot.loader import bot, dp
from bot.services.tasks import TaskService


@dp.callback_query_handler(lambda c: c.data == CommandEnum.LIST_TASK.value)
async def task_list(callback_query: types.CallbackQuery) -> None:
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, "Выберите промежуток времени", reply_markup=my_tasks_keyboard)


@dp.callback_query_handler(lambda c: c.data == CommandEnum.ALL_PLANED_TASKS.value)
async def all_planed_task(callback_query: types.CallbackQuery) -> None:
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    tasks = await TaskService.all_planed_tasks_for_user(callback_query.from_user.id)
    await bot.send_message(callback_query.from_user.id, tasks)
