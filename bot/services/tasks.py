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
