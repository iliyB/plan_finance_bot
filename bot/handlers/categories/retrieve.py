import re

from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.bot import bot, dp
from bot.keyboards.categories import retrieve_category_keyboard
from bot.states import FSMCategory


@dp.callback_query_handler(lambda c: re.match("category_[A-z0-9 _]*", c.data), state=FSMCategory.categories)
async def retrieve_category(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["category_name"] = callback_query.data.split("_")[-1]

    await bot.send_message(callback_query.from_user.id, "Действия", reply_markup=retrieve_category_keyboard)
    await FSMCategory.next()
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
