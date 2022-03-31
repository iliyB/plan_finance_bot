from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    Boolean,
    Text,
    SmallInteger,
    Date,
)
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from core.database import Base
from models import Category


class CompletedTask(Base):
    __tablename__ = "completed_task"

    completed_task_id = Column(Integer, primary_key=True, index=True, unique=True)
    feedback = Column(String, max_length=1024, null=True)
    completed_time = Column(DateTime)
    timeshift = Column(SmallInteger, min_value=1, null=True)


class Task(Base):
    __tablename__ = "task"

    task_id = Column(Integer, primary_key=True, index=True, unique=True)
    description = Column(Text, max_length=1024, null=True)
    links = Column(ARRAY(String), null=True)
    timeshift = Column(SmallInteger, min_value=1, null=True)
    planed_time = Column(Date, null=True)
    is_completed = Column(Boolean, default=False)

    user = relationship(
        "User", foreign_keys="task.user", back_populates="tasks"
    )
    category = relationship(
        Category, foreign_keys="task.category", back_populates="tasks"
    )
    completed_task = relationship(
        CompletedTask,
        foreign_keys="task.completed_task",
        back_populates="task",
        uselist=False
    )
