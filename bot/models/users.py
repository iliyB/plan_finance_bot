from sqlalchemy import CheckConstraint, Column, Integer
from sqlalchemy.orm import relationship

from bot.core.database import Base
from bot.models.many_to_many import UserCategory


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=False)
    categories = relationship("Category", secondary=UserCategory, back_populates="users")
    tasks = relationship("Task", back_populates="user")

    __table_args__ = (CheckConstraint(user_id > 0, name="check_positive_timeshift"), {})  # type: ignore
