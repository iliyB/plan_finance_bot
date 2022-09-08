from typing import Tuple

from models import User
from repositories.users import UserRepository
from schemes.users import UserCreateSchema


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def get_or_create(self, user_schema: UserCreateSchema) -> Tuple[User, bool]:
        return await self.user_repository.get_or_create(user_schema)
