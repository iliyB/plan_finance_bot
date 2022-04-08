import logging
from typing import Tuple

from bot.core.database import get_async_session
from bot.loggers.decorates import logging_decorator
from bot.models.users import User
from bot.schemes.users import UserIdScheme, UserScheme

logger = logging.getLogger(__name__)


class UserRepository:
    @staticmethod
    @logging_decorator(logger)
    async def get_or_create(user_id: int) -> Tuple[UserScheme, bool]:
        async with get_async_session() as session:
            user = await session.get(User, user_id)

            if not user:
                session.add(User(user_id=user_id))
                await session.commit()
                user = await session.get(User, user_id)
                return UserScheme.from_orm(user), True
            else:
                return UserScheme.from_orm(user), False
