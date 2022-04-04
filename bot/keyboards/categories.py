from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from bot.commands import CommandEnum

category_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
category_keyboard.add(KeyboardButton(CommandEnum.ADD_CATEGORY.value_with_slash))
category_keyboard.add(KeyboardButton(CommandEnum.LIST_CATEGORY.value_with_slash))
