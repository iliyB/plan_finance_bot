from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from bot.commands import CommandEnum

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add(KeyboardButton(CommandEnum.CATEGORY_KEYBOARD.value_with_slash))
