# import datetime
# import logging
# from typing import Callable, List, Optional
#
# from loggers.decorates import logging_decorator
# from models.tasks import CompletedTask, Task
# from models.users import User
# from repositories.categories import CategoryRepository
# from schemes.tasks import TaskCompleteScheme, TaskCreateScheme, TaskScheme
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select
# from sqlalchemy.orm import selectinload
#
# logger = logging.getLogger(__name__)
#
#
# class TaskRepository:
#     task_model = Task
#
#     def __init__(self, get_db_session: Callable[[], AsyncSession]) -> None:
#         self.get_db_session = get_db_session
#
#     async def create_task(self, task_create_data: TaskCreateScheme) -> None:
#         async with self.get_db_session() as session:
#             user = await session.get(User, task_create_data.user_id)
#             category, _ = await CategoryRepository.get_or_create_by_name(
#                 task_create_data.category_name
#             )
#             task = Task(
#                 description=task_create_data.description,
#                 planed_time=task_create_data.planed_time,
#                 timeshift=task_create_data.timeshift,
#                 category=category,
#                 user=user,
#             )
#             session.add(task)
#             await session.commit()
#
#     async def get_task(self, task_id: int) -> Optional[TaskScheme]:
#         async with self.get_db_session() as session:
#             task = await session.get(Task, task_id)
#             # task = await session.execute(
#             #     select(Task).where(Task.task_id == task_id).options(selectinload(Task.category))
#             # )
#             # task = task.scalars().first()
#             return TaskScheme.from_orm(task) if task else None
#
#     async def delete_task(self, task_id: int) -> None:
#         async with self.get_db_session() as session:
#             task = await session.get(Task, task_id)
#             if task:
#                 await session.delete(task)
#                 await session.commit()
#
#     async def completed_task(self, task_data: TaskCompleteScheme) -> None:
#         async with self.get_db_session() as session:
#             task = await session.get(Task, task_data.task_id)
#             if task:
#                 task.is_completed = True
#                 completed_task = CompletedTask(
#                     feedback=task_data.feedback,
#                     completed_time=task_data.completed_time,
#                     timeshift=task_data.timeshift,
#                     task=task,
#                 )
#                 session.add(task, completed_task)
#                 await session.commit()
#
#     async def planed_tasks_for_user(
#         self, user_id: int, delta_day: Optional[int] = None
#     ) -> List[TaskScheme]:
#         tasks = (
#             await TaskRepository._get_user_tasks(
#                 user_id,
#                 datetime.date.today(),
#                 datetime.date.today() + datetime.timedelta(days=delta_day),
#             )
#             if delta_day is not None
#             else await TaskRepository._get_user_tasks(user_id, datetime.date.today())
#         )
#
#         return [TaskScheme.from_orm(task) for task in tasks]
#
#     async def all_planed_tasks_for_user_on_period(
#         self, user_id: int, first_date: datetime.date, second_date: datetime.date
#     ) -> List[TaskScheme]:
#         tasks = await TaskRepository._get_user_tasks(user_id, first_date, second_date)
#         return [TaskScheme.from_orm(task) for task in tasks]
#
#     @staticmethod
#     async def _get_user_tasks(
#         session: AsyncSession,
#         user: User,
#         first_date: datetime.date,
#         second_date: Optional[datetime.date] = None,
#     ) -> List[Task]:
#         sql = select(Task).where(
#             Task.user == user,
#             Task.planed_time >= first_date,
#             # Task.completed_task == None,
#         )
#         if second_date:
#             sql = sql.where(Task.planed_time <= second_date)
#
#         tasks = await session.execute(sql)
#         return tasks.scalars().all()
