from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from commands import CommandEnum

main_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text=CommandEnum.CATEGORY_KEYBOARD.value)],
        [KeyboardButton(text=CommandEnum.TASK_KEYBOARD.value)],
    ],
)

reset_inline_button = InlineKeyboardButton(
    text=CommandEnum.RESET.value, callback_data=CommandEnum.RESET.value_with_slash
)
