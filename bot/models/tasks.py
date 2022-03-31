from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    Boolean,
    Text,
    SmallInteger,
    Date, CheckConstraint,
)
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from bot.core.database import Base


class BaseWithTimeshift(Base):
    __abstract__ = True

    timeshift = Column(SmallInteger, nullable=True)

    __table_args__ = (
        CheckConstraint("timeshift > 0", name="check_positive_timeshift"),
        {}
    )


class CompletedTask(BaseWithTimeshift):
    __tablename__ = "completed_task"

    completed_task_id = Column(Integer, primary_key=True, index=True, unique=True)
    feedback = Column(String, nullable=True)
    completed_time = Column(DateTime)


class Task(BaseWithTimeshift):
    __tablename__ = "task"

    task_id = Column(Integer, primary_key=True, index=True, unique=True)
    description = Column(Text, nullable=True)
    links = Column(ARRAY(String), nullable=True)
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
