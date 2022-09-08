import logging
from typing import Callable, List, Tuple

from models.categories import Category
from models.many_to_many import UserCategoryAssociatedTable
from models.users import User
from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

logger = logging.getLogger(__name__)


class CategoryRepository:
    category_model = Category
    user_model = User
    associate_model = UserCategoryAssociatedTable

    def __init__(self, get_db_session: Callable[[], AsyncSession]) -> None:
        self.get_db_session = get_db_session

    async def get_or_create_category_by_name(
        self, category_name: str
    ) -> Tuple[Category, bool]:
        async with self.get_db_session() as session:
            result = await session.execute(
                select(self.category_model).where(
                    self.category_model.category_name == category_name
                )
            )
            category = result.scalars().first()

            if not category:
                category = self.category_model(category_name=category_name)
                session.add(category)
                await session.commit()
                return category, True

        return category, False

    async def add_user_for_category(self, category_id: int, user_id: int) -> None:
        async with self.get_db_session() as session:
            try:
                await session.execute(
                    insert(self.associate_model).values(
                        category_id=category_id, user_id=user_id
                    )
                )
                await session.commit()
            except (IntegrityError, InvalidRequestError):
                pass

        return None

    async def list_user_categories(self, user: User) -> List[Category]:
        async with self.get_db_session() as session:
            result = await session.execute(
                select(self.category_model)
                .join(self.category_model.users)
                .where(self.user_model.user_id == user.user_id)
            )
            categories = result.scalars().all()

            return categories

    async def delete_category_for_user(self, category_name: str, user: User) -> None:
        async with self.get_db_session() as session:
            result = await session.execute(
                select(self.category_model)
                .where(self.category_model.category_name == category_name)
                .options(selectinload(self.category_model.users))
            )
            category = result.scalars().first()

            if not category:
                return None

            try:
                category.users.remove(user)
                session.add(category)
                await session.commit()
            except ValueError:
                pass

            return None
