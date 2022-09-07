from aiogram import Router, types
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from commands import CommandEnum
from keyboards.general import main_keyboard

from bot import bot

general_router = Router()


@general_router.message(
    Command(commands=[CommandEnum.START.name.lower(), CommandEnum.HELP.name.lower()])
)
async def start_command(message: types.Message) -> None:
    await message.answer("Hello, world!", reply_markup=main_keyboard)
    await bot.delete_message(message.from_user.id, message.message_id)


@general_router.message(Command(commands=[CommandEnum.RESET.name.lower()]), state="*")
@general_router.message(Text(text=CommandEnum.RESET.name, ignore_case=True), state="*")
async def reset_handler_state(message: types.Message, state: FSMContext) -> None:
    await bot.delete_message(message.from_user.id, message.message_id)
    if await state.get_state():
        await state.finish()


@general_router.callback_query(
    lambda c: c.data == CommandEnum.RESET.value_with_slash, state="*"
)
async def reset_handler_state_callback(
    callback_query: types.CallbackQuery, state: FSMContext
) -> None:
    await bot.delete_message(
        callback_query.from_user.id, callback_query.message.message_id
    )
    if await state.get_state():
        await state.finish()
