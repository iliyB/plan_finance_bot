import logging

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from utils.database import object_to_dict

from bot.core.database import get_async_session
from bot.models.users import User

log = logging.getLogger(__name__)


class AuthorizationMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, _: object) -> None:
        async with get_async_session() as session:
            user = await session.get(User, message.from_user.id)

            if not user:
                session.add(User(user_id=message.from_user.id))
                await session.commit()
                user = await session.get(User, message.from_user.id)

            user = object_to_dict(user)
            log.info(f"New user {user.get('user_id')}")
            log.info(f"Message from {user.get('user_id')}")
            setattr(message, "user", user)
