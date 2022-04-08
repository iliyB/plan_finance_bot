import logging
from typing import List, Tuple

from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from bot.core.database import get_async_session
from bot.loggers.decorates import logging_decorator
from bot.models.categories import Category
from bot.models.users import User
from bot.schemes.categories import CategoryNameScheme, CategoryScheme

logger = logging.getLogger(__name__)


class CategoryRepository:
    @staticmethod
    @logging_decorator(logger)
    async def get_or_create_by_name(category_name: str) -> Tuple[CategoryScheme, bool]:
        async with get_async_session() as session:
            category = await session.execute(select(Category).where(Category.category_name == category_name))
            category = category.scalars().first()

            if not category:
                session.add(Category(category_name=category_name))
                await session.commit()
                category = await session.execute(select(Category).where(Category.category_name == category_name))
                return CategoryScheme.from_orm(category.scalars().first()), True
            else:
                return CategoryScheme.from_orm(category), False

    @staticmethod
    @logging_decorator(logger)
    async def add_user_for_category(category_name: str, user_id: int) -> None:
        async with get_async_session() as session:
            category = await session.execute(
                select(Category).where(Category.category_name == category_name).options(selectinload(Category.users))
            )
            category = category.scalars().first()
            user = await session.get(User, user_id)
            category.users.append(user)
            session.add(category)
            await session.commit()

    @staticmethod
    @logging_decorator(logger)
    async def all_for_user(user_id: int) -> List[CategoryScheme]:
        async with get_async_session() as session:
            categories = await session.execute(select(Category).join(Category.users).where(User.user_id.in_([user_id])))
            return [CategoryScheme.from_orm(category) for category in categories.scalars().all()]

    @staticmethod
    @logging_decorator(logger)
    async def delete_category_for_user(category_name: str, user_id: int) -> None:
        async with get_async_session() as session:
            category = await session.execute(
                select(Category).where(Category.category_name == category_name).options(selectinload(Category.users))
            )
            category = category.scalars().first()

            if not category:
                return

            user = await session.get(User, user_id)
            category.users.remove(user)
            session.add(category)
            await session.commit()
