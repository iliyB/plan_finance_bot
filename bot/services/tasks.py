from bot.repositories.tasks import TaskRepository
from bot.schemes.tasks import TaskCreateScheme


class TaskService:
    @staticmethod
    async def create(task_create_data: TaskCreateScheme) -> None:
        await TaskRepository.create_task(task_create_data)
