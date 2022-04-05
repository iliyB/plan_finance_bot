from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.commands import CommandEnum

category_keyboard = InlineKeyboardMarkup()
category_keyboard.add(
    InlineKeyboardButton(CommandEnum.ADD_CATEGORY.value, callback_data=CommandEnum.ADD_CATEGORY.value)
)
category_keyboard.add(
    InlineKeyboardButton(CommandEnum.LIST_CATEGORY.value, callback_data=CommandEnum.LIST_CATEGORY.value)
)
