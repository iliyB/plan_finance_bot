import asyncio
import logging
import sys

from config import configs
from handlers.categories import category_router
from handlers.general import general_router
from middlewares.authorization import AuthorizationMiddleware

from bot import bot, dp


async def main() -> None:
    if configs.POLLING:
        dp.include_router(category_router)
        dp.include_router(general_router)
        dp.message.middleware(AuthorizationMiddleware())
        dp.callback_query.middleware(AuthorizationMiddleware())
        await dp.start_polling(bot)
    else:
        logging.critical("Webhook logics not supported)")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
