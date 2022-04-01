# from aiogram import types
# from aiogram.dispatcher import filters
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
#
#
#
import logging

from aiogram import types

from bot.loader import dp

log = logging.getLogger(__name__)


@dp.message_handler(commands=["categories"])
async def list_categories(message: types.Message) -> None:
    await message.answer(message.user)


#
# @dp.message_handler(filters.RegexpCommandsFilter(regexp_commands=['cat_([0-9]*)']))
# async def send_welcome(message: types.Message, regexp_command):
#     await message.answer(message.text.split("_")[-1])
#     await message.answer(await dp.get_category(int(message.text.split("_")[-1])) or "")
#
# @dp.message_handler(commands=["new"])
# async def inline_category_show(message: types.Message):
#     markup_request = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     categories = await dp.fetchall("category")
#     for category in categories:
#         button = InlineKeyboardButton(category.get("category_name"), callback_data='button1')
#         markup_request.row(button)
#     await message.reply("Выберите категорию", reply_markup=markup_request)
#
# # markup_request = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
# #     KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
# # ).add(
# #     KeyboardButton('Отправить свою локацию 🗺56️', request_location=True)
# # )
# #
# # @dp.message_handler(commands=['hi6'])
# # async def process_hi6_command(message: types.Message):
# #     await message.reply("Шестое - запрашиваем контакт и геолокацию\nЭти две кнопки не зависят друг от друга", reply_markup=markup_request)
# #
