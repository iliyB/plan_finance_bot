from typing import Dict

from aiogram import Bot, Dispatcher, types
from fastapi import FastAPI

from bot import config, loggers, middlewares
from bot.bot import bot
from bot.commands import CommandEnum
from bot.handlers import dp

app = FastAPI()


async def set_commands(bot: Bot) -> None:
    commands = [
        types.BotCommand(command=CommandEnum.START.name.lower(), description=CommandEnum.START.value),
        types.BotCommand(
            command=CommandEnum.CATEGORY_KEYBOARD.name.lower(), description=CommandEnum.CATEGORY_KEYBOARD.value
        ),
        types.BotCommand(command=CommandEnum.TASK_KEYBOARD.name.lower(), description=CommandEnum.TASK_KEYBOARD.value),
        types.BotCommand(command=CommandEnum.RESET.name.lower(), description=CommandEnum.RESET.value),
    ]
    await bot.set_my_commands(commands)


@app.on_event("startup")
async def on_startup() -> None:
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != config.WEBHOOK_URL:
        await bot.set_webhook(url=config.WEBHOOK_URL)
    await set_commands(bot)
    middlewares.setup(dp)
    loggers.setup()


@app.post(config.WEBHOOK_PATH)
async def bot_webhook(update: Dict) -> None:
    telegram_update = types.Update(**update)

    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.on_event("shutdown")
async def on_shutdown() -> None:
    await bot.session.close()
