from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

from bot.commands import CommandEnum

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add(KeyboardButton(CommandEnum.CATEGORY_KEYBOARD.value_with_slash))
main_keyboard.add(KeyboardButton(CommandEnum.TASK_KEYBOARD.value_with_slash))

reset_inline_button = InlineKeyboardButton(CommandEnum.RESET.value, callback_data=CommandEnum.RESET.value_with_slash)
