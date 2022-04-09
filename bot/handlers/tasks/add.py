import logging
import re
from typing import Dict

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram_calendar import SimpleCalendar, simple_cal_callback

from bot.commands import CommandEnum
from bot.keyboards.categories import create_retrieve_category_keyboard
from bot.loader import bot, dp
from bot.schemes.tasks import TaskCreateScheme
from bot.services.categories import CategoryService
from bot.services.tasks import TaskService
from bot.states import FSMAddTask


@dp.callback_query_handler(lambda c: c.data == CommandEnum.ADD_TASK.value, state=None)
async def add_task_start(callback_query: types.CallbackQuery) -> None:
    categories = await CategoryService.all_for_user(callback_query.from_user.id)
    if not categories:
        await bot.send_message(callback_query.from_user.id, "У вас ещё нет категорий")
        return

    await bot.send_message(
        callback_query.from_user.id, "Ваши категории", reply_markup=create_retrieve_category_keyboard(categories)
    )
    await FSMAddTask.category.set()
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)


@dp.callback_query_handler(lambda c: re.match("category_[A-z0-9 _]*", c.data), state=FSMAddTask.category)
async def add_description(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["category_name"] = callback_query.data.split("_")[-1]
    await bot.send_message(callback_query.from_user.id, "Введите описание задачи")
    await FSMAddTask.next()
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)


@dp.message_handler(state=FSMAddTask.description)
async def add_planed_time(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["description"] = message.text
    await bot.send_message(message.from_user.id, "Выберите дату", reply_markup=await SimpleCalendar().start_calendar())
    await FSMAddTask.next()
    await bot.delete_message(message.from_user.id, message.message_id)


@dp.callback_query_handler(simple_cal_callback.filter(), state=FSMAddTask.planed_time)
async def add_timeshift(callback_query: types.CallbackQuery, state: FSMContext, callback_data: Dict) -> None:
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if not selected:
        return
    async with state.proxy() as data:
        data["planed_time"] = date
    await bot.send_message(callback_query.from_user.id, "Укажите время на выполнение задачи")
    await FSMAddTask.next()
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)


@dp.message_handler(state=FSMAddTask.timeshift)
async def add_links(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        try:
            data["timeshift"] = int(message.text)
        except Exception:
            data["timeshift"] = None
        await TaskService.create(TaskCreateScheme(**data, user_id=message.from_user.id))
        await bot.send_message(message.from_user.id, data)
    await state.finish()
    await bot.delete_message(message.from_user.id, message.message_id)


# @dp.message_handler(state=FSMAddTask.links)
# async def end_add_task(message: types.Message, state: FSMContext) -> None:
#     async with state.proxy() as data:
#         data["links"] = [link.strip() for link in message.text.split(",")]
#         await bot.send_message(message.from_user.id, data)
#     await state.finish()
#     await bot.delete_message(message.from_user.id, message.message_id)
