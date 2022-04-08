from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from bot.models.tasks import CompletedTask, Task

CompletedTaskScheme = sqlalchemy_to_pydantic(CompletedTask)
TaskScheme = sqlalchemy_to_pydantic(Task)
