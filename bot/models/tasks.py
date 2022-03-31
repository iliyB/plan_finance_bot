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

from bot.core.database import Base


class CompletedTask(Base):
    __tablename__ = "completed_task"

    completed_task_id = Column(Integer, primary_key=True, index=True, unique=True)
    feedback = Column(String, max_length=1024, nullable=True)
    completed_time = Column(DateTime)
    timeshift = Column(SmallInteger, min_value=1, nullable=True)


class Task(Base):
    __tablename__ = "task"

    task_id = Column(Integer, primary_key=True, index=True, unique=True)
    description = Column(Text, max_length=1024, nullable=True)
    links = Column(ARRAY(String), nullable=True)
    timeshift = Column(SmallInteger, min_value=1, nullable=True)
    planed_time = Column(Date, nullable=True)
    is_completed = Column(Boolean, default=False)

    user = relationship(
        "User", foreign_keys="task.user", back_populates="tasks"
    )
    category = relationship(
        "Category", foreign_keys="task.category", back_populates="tasks"
    )
    completed_task = relationship(
        CompletedTask,
        foreign_keys="task.completed_task",
        back_populates="task",
        uselist=False
    )
