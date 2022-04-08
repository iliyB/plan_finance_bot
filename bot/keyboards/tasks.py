from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.commands import CommandEnum
from bot.keyboards.auxiliary import reset_button_inline

tasks_keyboard = InlineKeyboardMarkup()
tasks_keyboard.add(InlineKeyboardButton(CommandEnum.ADD_TASK.value, callback_data=CommandEnum.ADD_TASK.value))
tasks_keyboard.add(InlineKeyboardButton(CommandEnum.LIST_TASK.value, callback_data=CommandEnum.LIST_TASK.value))
tasks_keyboard.add(InlineKeyboardButton(CommandEnum.FILTER_TASK.value, callback_data=CommandEnum.FILTER_TASK.value))
tasks_keyboard.add(reset_button_inline)
