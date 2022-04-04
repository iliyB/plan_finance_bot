import logging

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from bot.services.users import UserService

logger = logging.getLogger(__name__)


class AuthorizationMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, _: object) -> None:
        user, is_created = await UserService.get_or_create(message.from_user.id)

        if is_created:
            logger.debug(f"New user {user.get('user_id')}")

        logger.debug(f"Message from {user.get('user_id')}")
        setattr(message, "user", user)
