from typing import Dict, List, Optional


class CategoryRepository:
    @staticmethod
    async def get_or_create(category_name: str) -> Optional[Dict]:
        pass

    @staticmethod
    async def add_user_for_category(category_name: str, user_id: str) -> None:
        pass

    @staticmethod
    async def all_for_user(user_id: str) -> Optional[List[Dict]]:
        pass
