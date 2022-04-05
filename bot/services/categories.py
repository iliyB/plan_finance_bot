import logging
from typing import Dict, List, Optional

from bot.repositories.categories import CategoryRepository

logger = logging.getLogger(__name__)


class CategoryService:
    @staticmethod
    async def add_for_user(category_name: str, user_id: int) -> None:
        logger.debug(f"Add category {category_name} for {user_id}")

        category, is_created = await CategoryRepository.get_or_create_by_name(category_name)

        if is_created:
            logger.debug(f"Category {category_name} created")

        await CategoryRepository.add_user_for_category(category_name, user_id)
        logger.debug(f"Category {category_name} add for {user_id}")
        return

    @staticmethod
    async def all_for_user(user_id: int) -> Optional[List[Dict]]:
        return await CategoryRepository.all_for_user(user_id)

    @staticmethod
    async def delete_for_user(category_name: str, user_id: int) -> None:
        pass