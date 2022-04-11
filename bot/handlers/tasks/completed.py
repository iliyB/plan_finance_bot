import ast
import json
import logging
from typing import Dict

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram_calendar import SimpleCalendar, simple_cal_callback

from bot.commands import CommandEnum
from bot.loader import bot, dp
from bot.states import FSMCompletedTask, FSMTask


@dp.callback_query_handler(lambda c: c.data == CommandEnum.COMPLETE_TASK.value, state=FSMTask.task)
async def start_complete_task(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    await FSMCompletedTask.feedback.set()
    await bot.send_message(callback_query.from_user.id, "Введите фидбек по задаче")
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)


@dp.message_handler(state=FSMCompletedTask.feedback)
async def feedback_task(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["feedback"] = message.text
        planed_time = json.loads(data["task"]).get("planed_time")

    await bot.send_message(
        message.from_user.id,
        f"Запланированная дата {planed_time}\nВыберите дату выполнения",
        reply_markup=await SimpleCalendar().start_calendar(),
    )
    await FSMCompletedTask.next()
    await bot.delete_message(message.from_user.id, message.message_id)


@dp.callback_query_handler(simple_cal_callback.filter(), state=FSMCompletedTask.completed_time)
async def completed_time_task(callback_query: types.CallbackQuery, state: FSMContext, callback_data: Dict) -> None:
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if not selected:
        return
    async with state.proxy() as data:
        data["completed_date"] = str(date.date())

    await bot.send_message(callback_query.from_user.id, "Укажите затраченное время")
    await FSMCompletedTask.next()
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)


@dp.message_handler(state=FSMCompletedTask.timeshift)
async def timeshift_task(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        try:
            data["timeshift"] = int(message.text)
        except Exception:
            data["timeshift"] = None
        await bot.send_message(message.from_user.id, data)

    await state.finish()
    await bot.delete_message(message.from_user.id, message.message_id)
