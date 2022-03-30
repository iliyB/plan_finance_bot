from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from core.database import Base
from models import UserCategory, User


class Category(Base):
    __tablename__ = 'category'

    category_id  = Column(Integer, primary_key=True, index=True, unique=True)
    category_name = Column(String, unique=True)
    users = relationship(User, secondary=UserCategory, back_populates='categories', null=True)
