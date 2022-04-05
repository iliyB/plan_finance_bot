import logging
from typing import Dict, List, Optional, Tuple

from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from bot.core.database import get_async_session
from bot.loggers.decorates import logging_decorator
from bot.models.categories import Category
from bot.models.users import User
from bot.utils.database import object_to_dict


class CategoryRepository:
    @staticmethod
    @logging_decorator
    async def get_or_create_by_name(category_name: str) -> Tuple[Dict, bool]:
        async with get_async_session() as session:
            category = await session.execute(select(Category).where(Category.category_name == category_name))
            category = category.scalars().first()

            if not category:
                session.add(Category(category_name=category_name))
                await session.commit()
                category = await session.execute(select(Category).where(Category.category_name == category_name))
                return object_to_dict(category.scalars().first()), True
            else:
                return object_to_dict(category), False

    @staticmethod
    @logging_decorator
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
    @logging_decorator
    async def all_for_user(user_id: int) -> Optional[List[Dict]]:
        async with get_async_session() as session:
            categories = await session.execute(select(Category).join(Category.users).where(User.user_id.in_([user_id])))
            return [object_to_dict(category) for category in categories.scalars().all()]
