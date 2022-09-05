import asyncio
import logging
import sys

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot import dp, bot
from config import configs

rout = Router()


@rout.message(Command(commands=["eqw"]))
async def command_start(message: Message):
    await message.answer("Нах")


async def main():
    if configs.POLLING:
        dp.include_router(rout)
        await dp.start_polling(bot)
    else:
        logging.critical("Webhook logics not supported")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
