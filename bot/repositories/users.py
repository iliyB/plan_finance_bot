import logging
from typing import Callable, Tuple

from loggers.decorates import logging_decorator
from models.users import User
from schemes.users import UserCreateSchema
from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)


class UserRepository:
    user_model = User

    def __init__(self, get_db_session: Callable[[], AsyncSession]) -> None:
        self.get_db_session = get_db_session

    # @logging_decorator(logger)
    async def get_or_create(self, user_schema: UserCreateSchema) -> Tuple[User, bool]:
        async with self.get_db_session() as session:
            user = await session.get(self.user_model, user_schema.user_id)

            if not user:
                user = self.user_model(**user_schema.dict())
                session.add(user)
                await session.commit()
                return user, True
            else:
                user, is_update = self._update_user_field(user, user_schema)
                if is_update:
                    session.add(user)
                    await session.commit()
                return user, False

    @staticmethod
    def _update_user_field(
        user: User, user_schema: UserCreateSchema
    ) -> Tuple[User, bool]:
        is_update = False

        for attr in user_schema.__fields__.keys():
            if getattr(user, attr) != getattr(user_schema, attr):
                setattr(user, attr, getattr(user_schema, attr))
                is_update = True

        return user, is_update
