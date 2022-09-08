from typing import List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from commands import CommandEnum
from keyboards.general import reset_inline_button
from models import Category


def create_categories_menu_keyboard() -> InlineKeyboardMarkup:
    """
    Создаёт инлайн клавиатуру меню категорий
    """
    categories_keyboard = InlineKeyboardBuilder()
    categories_keyboard.row(
        InlineKeyboardButton(
            text=CommandEnum.LIST_CATEGORY.value,
            callback_data=CommandEnum.LIST_CATEGORY.value,
        )
    )
    categories_keyboard.row(
        InlineKeyboardButton(
            text=CommandEnum.ADD_CATEGORY.value,
            callback_data=CommandEnum.ADD_CATEGORY.value,
        )
    )
    categories_keyboard.row(reset_inline_button)
    return categories_keyboard.as_markup()


def create_retrieve_category_menu_keyboard() -> InlineKeyboardMarkup:
    """
    Создаёт инлайн клавиатуру дейсвтий над категорией
    """
    retrieve_category_keyboard = InlineKeyboardBuilder()
    retrieve_category_keyboard.row(
        InlineKeyboardButton(
            text=CommandEnum.DELETE_CATEGORY.value,
            callback_data=CommandEnum.DELETE_CATEGORY.value,
        )
    )
    retrieve_category_keyboard.row(
        InlineKeyboardButton(
            text=CommandEnum.FILTER_CATEGORY.value,
            callback_data=CommandEnum.FILTER_CATEGORY.value,
        )
    )
    retrieve_category_keyboard.row(reset_inline_button)
    return retrieve_category_keyboard.as_markup()


def create_retrieve_category_keyboard(
    categories: List[Category],
) -> InlineKeyboardMarkup:
    """
    Создаёт инлайн клавиатуру листинга категорий
    """
    category_keyboard = InlineKeyboardBuilder()

    for category in categories:
        category_keyboard.row(
            InlineKeyboardButton(
                text=category.category_name,
                callback_data=f"category_{category.category_name}",
            )
        )

    category_keyboard.row(reset_inline_button)
    return category_keyboard.as_markup()


categories_keyboard = create_categories_menu_keyboard()
retrieve_category_keyboard = create_retrieve_category_menu_keyboard()
