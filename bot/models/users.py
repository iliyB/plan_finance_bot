from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from bot.core.database import Base
from bot.models.many_to_many import UserCategory


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(64), nullable=True)
    last_name = Column(String(64), nullable=True)
    username = Column(String(64), nullable=True)
    language_code = Column(String(16), nullable=True)

    timezone = Column(String(32), nullable=True)

    categories = relationship(
        "Category", secondary=UserCategory, back_populates="users"
    )
    tasks = relationship("Task", back_populates="user")
