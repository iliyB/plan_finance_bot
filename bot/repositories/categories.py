from typing import Dict, List, Optional

from bot.loggers.decorates import logging_decorator


class CategoryRepository:
    @staticmethod
    @logging_decorator
    async def get_or_create(category_name: str) -> Optional[Dict]:
        pass

    @staticmethod
    @logging_decorator
    async def add_user_for_category(category_name: str, user_id: str) -> None:
        pass

    @staticmethod
    @logging_decorator
    async def all_for_user(user_id: str) -> Optional[List[Dict]]:
        pass
