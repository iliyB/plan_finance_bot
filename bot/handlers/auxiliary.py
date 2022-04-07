from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.commands import CommandEnum
from bot.keyboards.auxiliary import main_keyboard
from bot.loader import bot, dp


@dp.message_handler(commands=[CommandEnum.START.value, CommandEnum.HELP.value])
async def start_command(message: types.Message) -> None:
    await message.answer("Hello", reply_markup=main_keyboard)
    await bot.delete_message(message.from_user.id, message.message_id)


@dp.message_handler(state="*", commands=[CommandEnum.RESET.value])
@dp.message_handler(Text(equals="reset", ignore_case=True), state="*")
async def reset_handler_state(message: types.Message, state: FSMContext) -> None:
    await bot.delete_message(message.from_user.id, message.message_id)
    if await state.get_state():
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == CommandEnum.RESET.value, state="*")
async def reset_handler_state_callback(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    if await state.get_state():
        await state.finish()
