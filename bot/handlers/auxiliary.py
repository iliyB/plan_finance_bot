import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.commands import CommandEnum
from bot.keyboards.auxiliary import main_keyboard
from bot.loader import dp

logger = logging.getLogger(__name__)


@dp.message_handler(commands=[CommandEnum.START.value, CommandEnum.HELP.value])
async def start_command(message: types.Message) -> None:
    await message.answer("Hello", reply_markup=main_keyboard)


@dp.message_handler(state="*", commands=[CommandEnum.RESET.value])
@dp.message_handler(Text(equals="reset", ignore_case=True), state="*")
async def reset_handler_state(message: types.Message, state: FSMContext) -> None:
    if await state.get_state() is None:
        return
    await state.finish()
    await message.reply("Ok")
