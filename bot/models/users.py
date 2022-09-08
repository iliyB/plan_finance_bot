from datetime import datetime

from core.database import Base
from models.many_to_many import UserCategoryAssociatedTable
from models.mixins import EqMixin
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship


class User(Base, EqMixin):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(64), nullable=True)
    last_name = Column(String(64), nullable=True)
    username = Column(String(64), nullable=True)
    language_code = Column(String(16), nullable=True)

    timezone = Column(String(32), nullable=True)

    categories = relationship(
        "Category", secondary=UserCategoryAssociatedTable, back_populates="users"
    )
    tasks = relationship("Task", back_populates="user")

    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
