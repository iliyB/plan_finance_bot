from typing import List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.emoji import emojize
from commands import CommandEnum
from keyboards.general import reset_inline_button
from schemes.tasks import TaskScheme

tasks_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=CommandEnum.ADD_TASK.value,
                callback_data=CommandEnum.ADD_TASK.value,
            )
        ],
        [
            InlineKeyboardButton(
                text=CommandEnum.LIST_TASK.value,
                callback_data=CommandEnum.LIST_TASK.value,
            )
        ],
        [
            InlineKeyboardButton(
                text=CommandEnum.FILTER_TASK.value,
                callback_data=CommandEnum.FILTER_TASK.value,
            )
        ],
        [reset_inline_button],
    ]
)

my_tasks_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=CommandEnum.TODAY_TASKS.value,
                callback_data=CommandEnum.TODAY_TASKS.value,
            )
        ],
        [
            InlineKeyboardButton(
                text=CommandEnum.WEEKLY_TASKS.value,
                callback_data=CommandEnum.WEEKLY_TASKS.value,
            )
        ],
        [
            InlineKeyboardButton(
                text=CommandEnum.PERIOD_TIME_TASKS.value,
                callback_data=CommandEnum.PERIOD_TIME_TASKS.value,
            )
        ],
        [
            InlineKeyboardButton(
                text=CommandEnum.ALL_PLANED_TASKS.value,
                callback_data=CommandEnum.ALL_PLANED_TASKS.value,
            )
        ],
        [reset_inline_button],
    ]
)

retrieve_task_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=CommandEnum.COMPLETE_TASK.value,
                callback_data=CommandEnum.COMPLETE_TASK.value,
            )
        ],
        [
            InlineKeyboardButton(
                text=CommandEnum.CHANGE_TASK.value,
                callback_data=CommandEnum.CHANGE_TASK.value,
            )
        ],
        [
            InlineKeyboardButton(
                text=CommandEnum.DELETE_TASK.value,
                callback_data=CommandEnum.DELETE_TASK.value,
            )
        ],
        [reset_inline_button],
    ]
)


def create_retrieve_task_keyboard(tasks: List[TaskScheme]) -> InlineKeyboardMarkup:
    task_list = []
    for task in tasks:
        emoji = emojize(":white_check_mark:") if task.is_completed else emojize(":x:")
        task_list.append(
            [
                InlineKeyboardButton(
                    text=f"{emoji}{task.description[:15]}:{task.planed_time}",
                    callback_data=f"task_{task.task_id}",
                )
            ]
        )
    task_keyboard = InlineKeyboardMarkup(
        inline_keyboard=task_list + [reset_inline_button]
    )
    return task_keyboard
