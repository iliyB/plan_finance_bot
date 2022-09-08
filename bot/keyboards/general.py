from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from commands import CommandEnum


def create_main_keyboard() -> ReplyKeyboardMarkup:
    """
    Создаёт клавиатуру главного меню
    """
    main_keyboard = ReplyKeyboardBuilder()
    main_keyboard.add(KeyboardButton(text=CommandEnum.CATEGORY_KEYBOARD.value))
    main_keyboard.add(KeyboardButton(text=CommandEnum.TASK_KEYBOARD.value))
    main_keyboard.adjust()
    return main_keyboard.as_markup(resize_keyboard=True)


main_keyboard = create_main_keyboard()

reset_inline_button = InlineKeyboardButton(
    text=CommandEnum.RESET.value, callback_data=CommandEnum.RESET.value_with_slash
)
