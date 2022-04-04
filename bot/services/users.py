from typing import Dict, Tuple

from bot.repositories.users import UserRepository


class UserService:
    @staticmethod
    async def get_or_create(user_id: int) -> Tuple[Dict, bool]:
        return await UserRepository.get_or_create(user_id)
