from typing import List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from commands import CommandEnum
from keyboards.general import reset_inline_button
from schemes.categories import CategoryScheme

categories_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=CommandEnum.LIST_CATEGORY.value,
                callback_data=CommandEnum.LIST_CATEGORY.value,
            )
        ],
        [
            InlineKeyboardButton(
                text=CommandEnum.ADD_CATEGORY.value,
                callback_data=CommandEnum.ADD_CATEGORY.value,
            )
        ],
        [reset_inline_button],
    ]
)


retrieve_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=CommandEnum.DELETE_CATEGORY.value,
                callback_data=CommandEnum.DELETE_CATEGORY.value,
            )
        ],
        [
            InlineKeyboardButton(
                text=CommandEnum.FILTER_CATEGORY.value,
                callback_data=CommandEnum.FILTER_CATEGORY.value,
            )
        ],
        [reset_inline_button],
    ]
)


def create_retrieve_category_keyboard(
    categories: List[CategoryScheme],
) -> InlineKeyboardMarkup:
    category_keyboard = InlineKeyboardMarkup(
        inline_keyboard=(
            [
                [
                    InlineKeyboardButton(
                        text=category.category_name,
                        callback_data=f"category_{category.category_name}",
                    )
                ]
                for category in categories
            ]
            + [reset_inline_button]
        )
    )
    return category_keyboard
