from datetime import date
from typing import Optional

from pydantic import BaseModel, Field
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from bot.models.tasks import CompletedTask, Task

CompletedTaskScheme = sqlalchemy_to_pydantic(CompletedTask)
TaskScheme = sqlalchemy_to_pydantic(Task)


class TaskCreateScheme(BaseModel):
    category_name: str = Field(max_length=32)
    description: str = Field(max_length=512)
    planed_time: date = Field(...)
    timeshift: Optional[int]
    user_id: int = Field(min_value=1)


class TaskCompleteScheme(BaseModel):
    task_id: int = Field(...)
    feedback: str = Field(max_length=512)
    completed_time: date = Field(...)
    timeshift: int = Field(max_value=20000)
