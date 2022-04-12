from aiogram import Dispatcher, types
from aiogram.utils import executor

from bot import loggers
from bot.commands import CommandEnum
from bot.loader import bot


async def set_commands(dispatcher: Dispatcher) -> None:
    commands = [
        types.BotCommand(command=CommandEnum.START.name.lower(), description=CommandEnum.START.value),
        types.BotCommand(
            command=CommandEnum.CATEGORY_KEYBOARD.name.lower(), description=CommandEnum.CATEGORY_KEYBOARD.value
        ),
        types.BotCommand(command=CommandEnum.TASK_KEYBOARD.name.lower(), description=CommandEnum.TASK_KEYBOARD.value),
        types.BotCommand(command=CommandEnum.RESET.name.lower(), description=CommandEnum.RESET.value),
    ]
    await bot.set_my_commands(commands)


if __name__ == "__main__":
    import middlewares
    from handlers import dp

    middlewares.setup(dp)
    loggers.setup()
    executor.start_polling(dp, skip_updates=True, on_startup=set_commands)
