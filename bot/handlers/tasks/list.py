import datetime
import logging
from typing import Dict

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram_calendar import SimpleCalendar, simple_cal_callback

from bot.bot import bot, dp
from bot.commands import CommandEnum
from bot.keyboards.tasks import create_retrieve_task_keyboard, my_tasks_keyboard
from bot.services.tasks import TaskService
from bot.states import FSMDatePeriod, FSMTask


@dp.callback_query_handler(lambda c: c.data == CommandEnum.LIST_TASK.value)
async def task_list(callback_query: types.CallbackQuery) -> None:
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, "Выберите промежуток времени", reply_markup=my_tasks_keyboard)


@dp.callback_query_handler(lambda c: c.data == CommandEnum.ALL_PLANED_TASKS.value, state=None)
async def all_planed_task(callback_query: types.CallbackQuery) -> None:
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    tasks = await TaskService.all_planed_tasks_for_user(callback_query.from_user.id)
    if tasks:
        await bot.send_message(callback_query.from_user.id, "Задачи", reply_markup=create_retrieve_task_keyboard(tasks))
        await FSMTask.tasks.set()
    else:
        await bot.send_message(callback_query.from_user.id, "У вас нет запланированных задач")


@dp.callback_query_handler(lambda c: c.data == CommandEnum.TODAY_TASKS.value, state=None)
async def task_on_today(callback_query: types.CallbackQuery) -> None:
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    tasks = await TaskService.all_planed_tasks_for_user_on_today(callback_query.from_user.id)
    if tasks:
        await bot.send_message(callback_query.from_user.id, "Задачи", reply_markup=create_retrieve_task_keyboard(tasks))
        await FSMTask.tasks.set()
    else:
        await bot.send_message(callback_query.from_user.id, "У вас нет запланированных задач")


@dp.callback_query_handler(lambda c: c.data == CommandEnum.WEEKLY_TASKS.value, state=None)
async def task_on_week(callback_query: types.CallbackQuery) -> None:
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    tasks = await TaskService.all_planed_tasks_for_user_on_week(callback_query.from_user.id)
    if tasks:
        await bot.send_message(callback_query.from_user.id, "Задачи", reply_markup=create_retrieve_task_keyboard(tasks))
        await FSMTask.tasks.set()
    else:
        await bot.send_message(callback_query.from_user.id, "У вас нет запланированных задач")


@dp.callback_query_handler(lambda c: c.data == CommandEnum.PERIOD_TIME_TASKS.value, state=None)
async def task_in_date_period(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await FSMDatePeriod.first_date.set()
    await bot.send_message(
        callback_query.from_user.id, "Выберите начальную дату", reply_markup=await SimpleCalendar().start_calendar()
    )


@dp.callback_query_handler(simple_cal_callback.filter(), state=FSMDatePeriod.first_date)
async def task_first_date(callback_query: types.CallbackQuery, state: FSMContext, callback_data: Dict) -> None:
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if not selected:
        return
    async with state.proxy() as data:
        data["first_date"] = str(date.date())
    await bot.send_message(
        callback_query.from_user.id, "Выберите конечную дату", reply_markup=await SimpleCalendar().start_calendar()
    )
    await FSMDatePeriod.next()
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)


@dp.callback_query_handler(simple_cal_callback.filter(), state=FSMDatePeriod.second_date)
async def task_second_date(callback_query: types.CallbackQuery, state: FSMContext, callback_data: Dict) -> None:
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if not selected:
        return
    async with state.proxy() as data:
        first_date = datetime.datetime.strptime(data["first_date"], "%Y-%m-%d")

        if first_date > date:
            await bot.send_message(callback_query.from_user.id, "Первая дата больше второй")
        else:
            tasks = await TaskService.all_planed_tasks_for_user_on_period(callback_query.from_user.id, first_date, date)
            if tasks:
                await bot.send_message(
                    callback_query.from_user.id, "Задачи", reply_markup=create_retrieve_task_keyboard(tasks)
                )
                await state.finish()
                await FSMTask.tasks.set()
            else:
                await bot.send_message(callback_query.from_user.id, "У вас нет запланированных задач")

    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
