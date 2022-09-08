import logging
from typing import List

from models import User
from repositories.categories import CategoryRepository
from schemes.categories import CategoryNameScheme, CategoryScheme

logger = logging.getLogger(__name__)


class CategoryService:
    def __init__(self, category_repository: CategoryRepository) -> None:
        self.category_repository = category_repository

    async def get_by_name(self, category_name: str) -> CategoryScheme:
        logger.debug(f"Get category {category_name}")
        category, _ = await self.category_repository.get_or_create_category_by_name(
            **CategoryNameScheme(category_name=category_name).dict()
        )
        return category

    async def add_for_user(self, category_name: str, user: User) -> None:
        # logger.debug(f"Add category {category_name} for {user.user_id}")

        (
            category,
            is_created,
        ) = await self.category_repository.get_or_create_category_by_name(
            **CategoryNameScheme(category_name=category_name).dict()
        )

        # if is_created:
        #     logger.debug(f"Category {category_name} created")

        await self.category_repository.add_user_for_category(
            category.category_id, user.user_id
        )
        # logger.debug(f"Category {category_name} add for {user.user_id}")
        return

    async def list_user_categories(self, user: User) -> List[CategoryScheme]:
        # logger.debug(f"All categories for {user.user_id}")
        return await self.category_repository.list_user_categories(user)

    # @staticmethod
    # async def delete_for_user(category_name: str, user_id: int) -> None:
    #     logger.debug(f"Delete category {category_name} for {user_id}")
    #     return await CategoryRepository.delete_category_for_user(
    #         **CategoryNameScheme(category_name=category_name).dict(),
    #     )
