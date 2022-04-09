import logging

from bot.core.database import get_async_session
from bot.loggers.decorates import logging_decorator
from bot.models.tasks import Task
from bot.models.users import User
from bot.repositories.categories import CategoryRepository
from bot.schemes.tasks import TaskCreateScheme

logger = logging.getLogger(__name__)


class TaskRepository:
    @staticmethod
    @logging_decorator(logger)
    async def create_task(task_create_data: TaskCreateScheme) -> None:
        async with get_async_session() as session:
            user = await session.get(User, task_create_data.user_id)
            category, _ = await CategoryRepository.get_or_create_by_name(
                task_create_data.category_name, return_pydantic=False
            )
            task = Task(
                description=task_create_data.description,
                planed_time=task_create_data.planed_time,
                timeshift=task_create_data.timeshift,
                category=category,
                user=user,
            )
            session.add(task)
            await session.commit()
