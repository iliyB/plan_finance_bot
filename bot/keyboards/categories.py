from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

category_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
category_keyboard.add(KeyboardButton("/add_category"))
category_keyboard.add(KeyboardButton("/categories"))
