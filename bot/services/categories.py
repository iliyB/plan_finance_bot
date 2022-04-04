import logging
from typing import Dict, List, Optional

from bot.repositories.categories import CategoryRepository

logger = logging.getLogger(__name__)


class CategoryService:
    @staticmethod
    async def add_for_user(category_name: str, user_id: int) -> None:
        logger.debug(f"Add category {category_name} for {user_id}")
        return await CategoryRepository.get_or_create_by_name(category_name)
        # Добавляем категория пользователю

    @staticmethod
    async def all_for_user(user_id: int) -> Optional[List[Dict]]:
        pass

    @staticmethod
    async def delete_for_user(category_name: str, user_id: int) -> None:
        pass
