from core.database import get_async_session
from repositories.categories import CategoryRepository
from repositories.users import UserRepository
from services.categories import CategoryService
from services.users import UserService

user_repository = UserRepository(get_async_session)
category_repository = CategoryRepository(get_async_session)

user_service = UserService(user_repository)
category_service = CategoryService(category_repository)


def get_user_service() -> UserService:
    return user_service


def get_category_service() -> CategoryService:
    return category_service
