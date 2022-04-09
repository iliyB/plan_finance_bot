import datetime
from typing import List

from bot.repositories.tasks import TaskRepository
from bot.schemes.tasks import TaskCreateScheme, TaskScheme


class TaskService:
    @staticmethod
    async def create(task_create_data: TaskCreateScheme) -> None:
        await TaskRepository.create_task(task_create_data)

    @staticmethod
    async def all_planed_tasks_for_user(user_id: int) -> List[TaskScheme]:
        return await TaskRepository.all_planed_tasks_for_user(user_id)

    @staticmethod
    async def all_planed_tasks_for_user_on_today(user_id: int) -> List[TaskScheme]:
        return await TaskRepository.all_planed_tasks_for_user_on_today(user_id)

    @staticmethod
    async def all_planed_tasks_for_user_on_week(user_id: int) -> List[TaskScheme]:
        return await TaskRepository.all_planed_tasks_for_user_on_week(user_id)

    @staticmethod
    async def all_planed_tasks_for_user_on_period(
        user_id: int, first_date: datetime.date, second_date: datetime.date
    ) -> List[TaskScheme]:
        return await TaskRepository.all_planed_tasks_for_user_on_period(user_id, first_date, second_date)
