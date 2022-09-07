from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import CallbackQuery, Message
from commands import CommandEnum

# from services.categories import CategoryService
from keyboards.categories import categories_keyboard
from models import User

from bot import bot

category_router = Router()


@category_router.message(Command(commands=CommandEnum.CATEGORY_KEYBOARD.name.lower()))
@category_router.message(
    Text(text=CommandEnum.CATEGORY_KEYBOARD.value, ignore_case=True), state="*"
)
async def category_keyboard_view(message: Message, user: User) -> None:
    await message.answer("Меню категорий", reply_markup=categories_keyboard)
    await bot.delete_message(message.from_user.id, message.message_id)


@category_router.callback_query(
    lambda c: c.data == CommandEnum.LIST_CATEGORY.value, state=None
)
async def list_categories(callback_query: CallbackQuery, user: User) -> None:
    await bot.send_message(callback_query.from_user.id, "wqeqe")
    # categories = await CategoryService.all_for_user(callback_query.from_user.id)
