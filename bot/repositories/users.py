from typing import Dict, Tuple

from bot.core.database import get_async_session
from bot.models.users import User
from bot.utils.database import object_to_dict


class UserRepository:
    @staticmethod
    async def get_or_create(user_id: int) -> Tuple[Dict, bool]:
        async with get_async_session() as session:
            user = await session.get(User, user_id)

            if not user:
                session.add(User(user_id=user_id))
                await session.commit()
                user = await session.get(User, user_id)
                return object_to_dict(user), True
            else:
                return object_to_dict(user), False
