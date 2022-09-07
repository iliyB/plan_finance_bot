import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware, types
from aiogram.types import CallbackQuery, Message, TelegramObject
from schemes.users import UserCreateSchema
from services.users import UserService

logger = logging.getLogger(__name__)


class AuthorizationMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        if not isinstance(event, (Message, CallbackQuery)):
            return

        logger.debug(f"Message from {event.from_user.id}")

        user_schema = UserCreateSchema(
            user_id=event.from_user.id,
            username=event.from_user.username,
            first_name=event.from_user.first_name,
            last_name=event.from_user.last_name,
            language_code=event.from_user.language_code,
        )

        user, is_created = await UserService().get_or_create(user_schema)

        if is_created:
            logger.debug(f"New user {user.user_id}")

        data["user"] = user

        result = await handler(event, data)
        return result
