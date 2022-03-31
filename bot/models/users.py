from sqlalchemy import Integer, Column
from sqlalchemy.orm import relationship

from bot.core.database import Base
from bot.models.many_to_many import UserCategory


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=False)
    category_ids = relationship("Category", secondary=UserCategory, back_populates='users')
