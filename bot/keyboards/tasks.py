import logging
from typing import List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.emoji import emojize

from bot.commands import CommandEnum
from bot.keyboards.auxiliary import reset_inline_button
from bot.schemes.tasks import TaskScheme

tasks_keyboard = InlineKeyboardMarkup()
tasks_keyboard.add(
    InlineKeyboardButton(
        CommandEnum.ADD_TASK.value, callback_data=CommandEnum.ADD_TASK.value
    )
)
tasks_keyboard.add(
    InlineKeyboardButton(
        CommandEnum.LIST_TASK.value, callback_data=CommandEnum.LIST_TASK.value
    )
)
tasks_keyboard.add(
    InlineKeyboardButton(
        CommandEnum.FILTER_TASK.value, callback_data=CommandEnum.FILTER_TASK.value
    )
)
tasks_keyboard.add(reset_inline_button)

my_tasks_keyboard = InlineKeyboardMarkup()
my_tasks_keyboard.add(
    InlineKeyboardButton(
        CommandEnum.TODAY_TASKS.value, callback_data=CommandEnum.TODAY_TASKS.value
    )
)
my_tasks_keyboard.add(
    InlineKeyboardButton(
        CommandEnum.WEEKLY_TASKS.value, callback_data=CommandEnum.WEEKLY_TASKS.value
    )
)
my_tasks_keyboard.add(
    InlineKeyboardButton(
        CommandEnum.PERIOD_TIME_TASKS.value,
        callback_data=CommandEnum.PERIOD_TIME_TASKS.value,
    )
)
my_tasks_keyboard.add(
    InlineKeyboardButton(
        CommandEnum.ALL_PLANED_TASKS.value,
        callback_data=CommandEnum.ALL_PLANED_TASKS.value,
    )
)
my_tasks_keyboard.add(reset_inline_button)

retrieve_task_keyboard = InlineKeyboardMarkup()
retrieve_task_keyboard.add(
    InlineKeyboardButton(
        CommandEnum.COMPLETE_TASK.value, callback_data=CommandEnum.COMPLETE_TASK.value
    )
)
retrieve_task_keyboard.add(
    InlineKeyboardButton(
        CommandEnum.CHANGE_TASK.value, callback_data=CommandEnum.CHANGE_TASK.value
    )
)
retrieve_task_keyboard.add(
    InlineKeyboardButton(
        CommandEnum.DEL_TASK.value, callback_data=CommandEnum.DEL_TASK.value
    )
)
retrieve_task_keyboard.add(reset_inline_button)


def create_retrieve_task_keyboard(tasks: List[TaskScheme]) -> InlineKeyboardMarkup:
    task_keyboard = InlineKeyboardMarkup()
    for task in tasks:
        emoji = emojize(":white_check_mark:") if task.is_completed else emojize(":x:")
        task_keyboard.add(
            InlineKeyboardButton(
                f"{emoji}{task.description[:15]}:{task.planed_time}",
                callback_data=f"task_{task.task_id}",
            )
        )
    task_keyboard.add(reset_inline_button)
    return task_keyboard
