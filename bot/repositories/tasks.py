import datetime
import logging
from typing import List, Optional

from sqlalchemy.future import select

from bot.core.database import get_async_session
from bot.loggers.decorates import logging_decorator
from bot.models.tasks import Task
from bot.models.users import User
from bot.repositories.categories import CategoryRepository
from bot.schemes.tasks import TaskCreateScheme, TaskScheme

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

    @staticmethod
    @logging_decorator(logger)
    async def get_task(task_id: int) -> Optional[TaskScheme]:
        async with get_async_session() as session:
            task = await session.get(Task, task_id)
            return TaskScheme.from_orm(task) if task else None

    @staticmethod
    @logging_decorator(logger)
    async def planed_tasks_for_user(user_id: int, delta_day: Optional[int] = None) -> List[TaskScheme]:
        tasks = (
            await TaskRepository._get_user_tasks(
                user_id, datetime.date.today(), datetime.date.today() + datetime.timedelta(days=delta_day)
            )
            if delta_day is not None
            else await TaskRepository._get_user_tasks(user_id, datetime.date.today())
        )

        return [TaskScheme.from_orm(task) for task in tasks]

    @staticmethod
    @logging_decorator(logger)
    async def all_planed_tasks_for_user_on_period(
        user_id: int, first_date: datetime.date, second_date: datetime.date
    ) -> List[TaskScheme]:
        tasks = await TaskRepository._get_user_tasks(user_id, first_date, second_date)
        return [TaskScheme.from_orm(task) for task in tasks]

    @staticmethod
    async def _get_user_tasks(
        user_id: int, first_date: datetime.date, second_date: Optional[datetime.date] = None
    ) -> List[Task]:
        async with get_async_session() as session:
            user = await session.get(User, user_id)
            sql = select(Task).where(
                Task.user == user,
                Task.planed_time >= first_date,
                Task.completed_task == None,
            )
            if second_date:
                sql = sql.where(Task.planed_time <= second_date)

            tasks = await session.execute(sql)
            return tasks.scalars().all()
