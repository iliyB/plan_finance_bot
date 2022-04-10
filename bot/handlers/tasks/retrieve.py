import logging
import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hbold

from bot.keyboards.tasks import retrieve_task_keyboard
from bot.loader import bot, dp
from bot.services.tasks import TaskService
from bot.states import FSMTask


@dp.callback_query_handler(lambda c: re.match("task_[0-9]*", c.data), state=FSMTask.tasks)
async def retrieve_task(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    task = await TaskService.get_task(int(callback_query.data.split("_")[-1]))
    if not task:
        await state.finish()
        return
    async with state.proxy() as data:
        data["task"] = task.json()
        data["task_id"] = task.task_id

    task_card = (
        f"{hbold(task.description)}\n"
        f"{hbold(task.category_id)}\n"
        f"{hbold(task.planed_time)}\n"
        f"{hbold(task.timeshift)}"
    )
    await FSMTask.next()
    await bot.send_message(callback_query.from_user.id, task_card, reply_markup=retrieve_task_keyboard)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
