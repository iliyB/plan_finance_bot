from core.database import Base
from models.mixins import EqMixin
from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    SmallInteger,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship


class BaseWithTimeshift(Base):
    __abstract__ = True

    timeshift = Column(SmallInteger, nullable=True)

    __table_args__ = (
        CheckConstraint("timeshift > 0", name="check_positive_timeshift"),
    )


class CompletedTask(BaseWithTimeshift, EqMixin):
    __tablename__ = "completed_task"

    completed_task_id = Column(Integer, primary_key=True)
    feedback = Column(String, nullable=True)
    completed_time = Column(DateTime)

    task_id = Column(Integer, ForeignKey("task.task_id"), unique=True)
    task = relationship("Task", back_populates="completed_task", uselist=False)


class Task(BaseWithTimeshift, EqMixin):
    __tablename__ = "task"

    task_id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=True)
    links = Column(ARRAY(String), nullable=True)

    planed_start_date = Column(Date, nullable=True)
    planed_end_date = Column(Date, nullable=True)
    is_completed = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("user.user_id"))
    user = relationship("User", back_populates="tasks")

    category_id = Column(Integer, ForeignKey("category.category_id"))
    category = relationship("Category", back_populates="tasks")

    completed_task = relationship(CompletedTask, back_populates="task")
