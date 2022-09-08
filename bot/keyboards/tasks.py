from typing import List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.emoji import emojize
from aiogram.utils.keyboard import InlineKeyboardBuilder
from commands import CommandEnum
from keyboards.general import reset_inline_button
from models import Task


def create_tasks_menu_keyboard() -> InlineKeyboardMarkup:
    """
    Создаёт инлайн клавиатуру основного меню задач
    """
    tasks_keyboard = InlineKeyboardBuilder()
    tasks_keyboard.row(
        InlineKeyboardButton(
            text=CommandEnum.ADD_TASK.value,
            callback_data=CommandEnum.ADD_TASK.value,
        )
    )
    tasks_keyboard.row(
        InlineKeyboardButton(
            text=CommandEnum.LIST_TASK.value,
            callback_data=CommandEnum.LIST_TASK.value,
        )
    )
    tasks_keyboard.row(
        InlineKeyboardButton(
            text=CommandEnum.FILTER_TASK.value,
            callback_data=CommandEnum.FILTER_TASK.value,
        )
    )
    tasks_keyboard.row(reset_inline_button)
    return tasks_keyboard.as_markup()


def create_my_tasks_keyboard() -> InlineKeyboardMarkup:
    """
    Создаёт инлайн клавиатуру фильтрации задач
    """
    my_tasks_keyboard = InlineKeyboardBuilder()
    my_tasks_keyboard.row(
        InlineKeyboardButton(
            text=CommandEnum.TODAY_TASKS.value,
            callback_data=CommandEnum.TODAY_TASKS.value,
        )
    )
    my_tasks_keyboard.row(
        InlineKeyboardButton(
            text=CommandEnum.WEEKLY_TASKS.value,
            callback_data=CommandEnum.WEEKLY_TASKS.value,
        )
    )
    my_tasks_keyboard.row(
        InlineKeyboardButton(
            text=CommandEnum.PERIOD_TIME_TASKS.value,
            callback_data=CommandEnum.PERIOD_TIME_TASKS.value,
        )
    )
    my_tasks_keyboard.row(
        InlineKeyboardButton(
            text=CommandEnum.ALL_PLANED_TASKS.value,
            callback_data=CommandEnum.ALL_PLANED_TASKS.value,
        )
    )
    my_tasks_keyboard.row(reset_inline_button)
    return my_tasks_keyboard.as_markup()


def create_retrieve_task_menu_keyboard() -> InlineKeyboardMarkup:
    """
    Создаёт инлайн клавиатуру задачи
    """
    retrieve_task_keyboard = InlineKeyboardBuilder()
    retrieve_task_keyboard.row(
        InlineKeyboardButton(
            text=CommandEnum.COMPLETE_TASK.value,
            callback_data=CommandEnum.COMPLETE_TASK.value,
        )
    )
    retrieve_task_keyboard.row(
        InlineKeyboardButton(
            text=CommandEnum.CHANGE_TASK.value,
            callback_data=CommandEnum.CHANGE_TASK.value,
        )
    )
    retrieve_task_keyboard.row(
        InlineKeyboardButton(
            text=CommandEnum.DELETE_TASK.value,
            callback_data=CommandEnum.DELETE_TASK.value,
        )
    )
    retrieve_task_keyboard.row(reset_inline_button)
    return retrieve_task_keyboard.as_markup()


def create_retrieve_task_keyboard(tasks: List[Task]) -> InlineKeyboardMarkup:
    """
    Создаёт инлайн клавиатуру листинга задач
    """
    task_keyboard = InlineKeyboardBuilder()

    for task in tasks:
        emoji = emojize(":white_check_mark:") if task.is_completed else emojize(":x:")
        task_keyboard.row(
            InlineKeyboardButton(
                text=f"{emoji}{task.description[:15]}:{task.planed_start_date}",
                callback_data=f"task_{task.task_id}",
            )
        )

    task_keyboard.row(reset_inline_button)
    return task_keyboard.as_markup()


tasks_keyboard = create_tasks_menu_keyboard()
my_tasks_keyboard = create_my_tasks_keyboard()
retrieve_task_keyboard = create_retrieve_task_menu_keyboard()
