from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.commands import CommandEnum
from bot.keyboards.auxiliary import reset_inline_button

tasks_keyboard = InlineKeyboardMarkup()
tasks_keyboard.add(InlineKeyboardButton(CommandEnum.ADD_TASK.value, callback_data=CommandEnum.ADD_TASK.value))
tasks_keyboard.add(InlineKeyboardButton(CommandEnum.LIST_TASK.value, callback_data=CommandEnum.LIST_TASK.value))
tasks_keyboard.add(InlineKeyboardButton(CommandEnum.FILTER_TASK.value, callback_data=CommandEnum.FILTER_TASK.value))
tasks_keyboard.add(reset_inline_button)

my_tasks_keyboard = InlineKeyboardMarkup()
my_tasks_keyboard.add(InlineKeyboardButton(CommandEnum.TODAY_TASKS.value, callback_data=CommandEnum.TODAY_TASKS.value))
my_tasks_keyboard.add(
    InlineKeyboardButton(CommandEnum.WEEKLY_TASKS.value, callback_data=CommandEnum.WEEKLY_TASKS.value)
)
my_tasks_keyboard.add(
    InlineKeyboardButton(CommandEnum.PERIOD_TIME_TASKS.value, callback_data=CommandEnum.PERIOD_TIME_TASKS.value)
)
my_tasks_keyboard.add(
    InlineKeyboardButton(CommandEnum.ALL_PLANED_TASKS.value, callback_data=CommandEnum.ALL_PLANED_TASKS.value)
)
my_tasks_keyboard.add(reset_inline_button)
