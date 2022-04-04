from typing import Dict, List, Optional


class CategoryService:
    @staticmethod
    async def add_for_user(category_name: str, user_id: int) -> None:
        pass

    @staticmethod
    async def all_for_user(user_id: int) -> Optional[List[Dict]]:
        pass

    @staticmethod
    async def delete_for_user(category_name: str, user_id: int) -> None:
        pass
