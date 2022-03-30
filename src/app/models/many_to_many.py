from sqlalchemy import Column, Integer, ForeignKey

from core.database import Base
from models import User, Category


class UserCategory(Base):
    __tablename__ = 'user_category'

    id = Column(Integer, primary_key=True, unqiue=True)
    user_id = Column(Integer, ForeignKey(User))
    category_id = Column(Integer, ForeignKey(Category))
