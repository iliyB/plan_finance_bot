from sqlalchemy import Column, Integer, ForeignKey

from bot.core.database import Base


class UserCategory(Base):
    __tablename__ = 'user_category'

    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    category_id = Column(Integer, ForeignKey("category.category_id"))
