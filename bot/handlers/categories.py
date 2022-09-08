from aiogram import F, Router
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from commands import CommandEnum

# from services.categories import CategoryService
from keyboards.categories import categories_keyboard, create_retrieve_category_keyboard
from middlewares.categories import CategoryServiceMiddleware
from models import User
from services.categories import CategoryService
from states import FSMAddCategory, FSMCategory

from bot import bot

category_router = Router()

category_service_middleware = CategoryServiceMiddleware()
category_router.message.middleware(category_service_middleware)
category_router.callback_query.middleware(category_service_middleware)


@category_router.message(Command(commands=CommandEnum.CATEGORY_KEYBOARD.name.lower()))
@category_router.message(
    Text(text=CommandEnum.CATEGORY_KEYBOARD.value, ignore_case=True), state="*"
)
async def category_keyboard_view(message: Message) -> None:
    await message.answer("Меню категорий", reply_markup=categories_keyboard)
    await bot.delete_message(message.from_user.id, message.message_id)


@category_router.callback_query(F.data == CommandEnum.LIST_CATEGORY.value, state=None)
async def list_categories(
    callback_query: CallbackQuery,
    state: FSMContext,
    user: User,
    category_service: CategoryService,
) -> None:
    categories = await category_service.list_user_categories(user)
    if categories:
        await state.set_state(FSMCategory.categories)
        await bot.send_message(
            callback_query.from_user.id,
            "Ваши категории",
            reply_markup=create_retrieve_category_keyboard(categories),
        )
    else:
        await bot.send_message(callback_query.from_user.id, "У вас ещё нет категорий")

    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(
        callback_query.from_user.id, callback_query.message.message_id
    )


@category_router.callback_query(
    lambda c: c.data == CommandEnum.ADD_CATEGORY.value, state=None
)
async def add_category_start(callback_query: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(FSMAddCategory.command)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Введите название категории")
    await bot.delete_message(
        callback_query.from_user.id, callback_query.message.message_id
    )


@category_router.message(state=FSMAddCategory.command)
async def add_category_name(
    message: Message, state: FSMContext, user: User, category_service: CategoryService
) -> None:
    await category_service.add_for_user(message.text, user)
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.send_message(message.from_user.id, f"Категория {message.text} добавлена")
    await state.clear()
