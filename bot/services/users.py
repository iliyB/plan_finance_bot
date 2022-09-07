from typing import Tuple

from core.database import get_async_session
from models import User
from py_singleton import singleton
from repositories.users import UserRepository
from schemes.users import UserCreateSchema


@singleton
class UserService:
    user_repository = UserRepository(get_async_session)

    async def get_or_create(self, user_schema: UserCreateSchema) -> Tuple[User, bool]:
        return await self.user_repository.get_or_create(user_schema)
