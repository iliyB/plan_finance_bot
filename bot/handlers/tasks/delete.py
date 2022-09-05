from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.bot import bot, dp
from bot.commands import CommandEnum
from bot.services.tasks import TaskService
from bot.states import FSMTask


@dp.callback_query_handler(
    lambda c: c.data == CommandEnum.DEL_TASK.value, state=FSMTask.task
)
async def delete_task(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    async with state.proxy() as data:
        task_id = data.get("task_id")

    await TaskService.delete_task(int(task_id))
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(
        callback_query.from_user.id, callback_query.message.message_id
    )
    await bot.send_message(callback_query.from_user.id, "Задача удалена")
    await state.finish()
