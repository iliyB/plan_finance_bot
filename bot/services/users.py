from typing import Tuple

from bot.repositories.users import UserRepository
from bot.schemes.users import UserIdScheme, UserScheme


class UserService:
    @staticmethod
    async def get_or_create(user_id: int) -> Tuple[UserScheme, bool]:
        return await UserRepository.get_or_create(**UserIdScheme(user_id=user_id).dict())
